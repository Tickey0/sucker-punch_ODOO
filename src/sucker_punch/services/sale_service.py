"""Guarda una venta en Odoo: pedido -> entrega (baja el stock) -> factura -> pagos.

Cada llamada JSON-2 es una transacción aparte. Si una falla a la mitad, lo anterior ya
quedó guardado; por eso el error dice qué alcanzó a hacerse.

Formas de pago: se registra un pago por cada una, en el diario que tenga su forma de
pago SRI (Facturación → Configuración → Diarios). El XML del SRI toma la forma de pago
del diario de cada pago.
"""

from ..models.payment import METHODS, Payment
from ..models.sale_line import SaleLine
from ..models.sale_result import SaleResult
from .odoo_client import OdooClient, OdooError

# Forma de pago de la app → código SRI (tabla 24 de la ficha técnica)
SRI_CODES = {
    'cash': '01',  # sin utilización del sistema financiero
    'card': '19',  # tarjeta de crédito
    'transfer': '20',  # otros con utilización del sistema financiero
    'other': '20',
}

PAYMENT_STATES = {
    'paid': 'Pagada',
    'in_payment': 'En proceso de pago',
    'partial': 'Pagada parcialmente',
    'not_paid': 'No pagada',
}


class SaleError(Exception):
    """La venta no se pudo guardar completa."""


class SaleService:
    def __init__(self, odoo: OdooClient):
        self.odoo = odoo
        self._sri_ids = None  # {código SRI: id de l10n_ec.sri.payment}

    def _context(self, **extra) -> dict:
        return {**self.odoo.context, **extra}

    def _sri_payment_ids(self) -> dict[str, int]:
        """Formas de pago SRI de Odoo. Vacío si no está la localización de Ecuador."""
        if self._sri_ids is None:
            try:
                rows = self.odoo.call(
                    'l10n_ec.sri.payment', 'search_read', domain=[], fields=['code']
                )
            except OdooError:
                rows = []
            self._sri_ids = {row['code']: row['id'] for row in rows}
        return self._sri_ids

    def _journal(self, method: str) -> int:
        """Diario para esa forma de pago: el que tiene su código SRI. Si ninguno lo tiene,
        el de Efectivo (solo para efectivo) o el de Banco."""
        if self._sri_payment_ids():
            try:
                ids = self.odoo.call(
                    'account.journal',
                    'search',
                    limit=1,
                    domain=[
                        ['type', 'in', ['cash', 'bank']],
                        ['l10n_ec_sri_payment_id.code', '=', SRI_CODES[method]],
                    ],
                )
            except OdooError:  # sin el módulo l10n_ec_base no existe ese campo
                ids = []
            if ids:
                return ids[0]
        for journal_type in ('cash', 'bank') if method == 'cash' else ('bank',):
            ids = self.odoo.call(
                'account.journal', 'search', limit=1, domain=[['type', '=', journal_type]]
            )
            if ids:
                return ids[0]
        raise OdooError(f'No hay un diario para {METHODS[method]} en Odoo.')

    def save(self, lines: list[SaleLine], customer: int, payment: Payment) -> SaleResult:
        """Guarda la venta a nombre del cliente (id de res.partner) con esos pagos."""
        odoo = self.odoo
        done = []
        amounts = payment.amounts()
        step = 'crear el pedido de venta'
        try:
            order_id = odoo.call(
                'sale.order',
                'create',
                vals_list=[
                    {
                        'partner_id': customer,
                        # Sin posición fiscal: el IVA es el del producto, el mismo que
                        # muestra la factura de la app
                        'fiscal_position_id': False,
                        'order_line': [
                            [
                                0,
                                0,
                                {
                                    'product_id': line.product.id,
                                    'product_uom_qty': line.quantity,
                                    'price_unit': line.price,
                                },
                            ]
                            for line in lines
                        ],
                    }
                ],
            )[0]
            order = odoo.call('sale.order', 'read', ids=[order_id], fields=['name'])[0]
            done.append(f'pedido {order["name"]}')

            step = 'confirmar el pedido'
            odoo.call('sale.order', 'action_confirm', ids=[order_id])
            done.append('pedido confirmado')

            step = 'validar la entrega (bajar el stock)'
            pickings = odoo.call(
                'stock.picking',
                'search_read',
                fields=['move_ids'],
                domain=[
                    ['sale_id', '=', order_id],
                    ['state', 'not in', ['done', 'cancel']],
                ],
            )
            for picking in pickings:
                moves = odoo.call(
                    'stock.move',
                    'read',
                    ids=picking['move_ids'],
                    fields=['product_uom_qty'],
                )
                for move in moves:
                    odoo.call(
                        'stock.move',
                        'write',
                        ids=[move['id']],
                        vals={'quantity': move['product_uom_qty'], 'picked': True},
                    )
                result = odoo.call(
                    'stock.picking',
                    'button_validate',
                    ids=[picking['id']],
                    context=self._context(skip_backorder=True, skip_sms=True),
                )
                if isinstance(result, dict) and result.get('res_model'):
                    raise OdooError(
                        'Odoo pidió confirmar algo en la entrega '
                        f'({result["res_model"]}).'
                    )
            done.append('entrega validada')

            step = 'crear la factura'
            order_context = self._context(
                active_model='sale.order', active_ids=[order_id]
            )
            wizard = odoo.call(
                'sale.advance.payment.inv',
                'create',
                context=order_context,
                vals_list=[{'advance_payment_method': 'delivered'}],
            )[0]
            odoo.call(
                'sale.advance.payment.inv',
                'create_invoices',
                ids=[wizard],
                context=order_context,
            )
            invoice_id = odoo.call(
                'sale.order', 'read', ids=[order_id], fields=['invoice_ids']
            )[0]['invoice_ids'][-1]

            # La forma de pago SRI de la factura: la del mayor valor (el XML la usa si
            # se genera antes de que existan los pagos)
            main_method = max(amounts, key=amounts.get, default='cash')
            sri_id = self._sri_payment_ids().get(SRI_CODES[main_method])
            if sri_id:
                step = 'poner la forma de pago SRI en la factura'
                odoo.call(
                    'account.move',
                    'write',
                    ids=[invoice_id],
                    vals={'l10n_ec_sri_payment_id': sri_id},
                )

            step = 'confirmar la factura'
            odoo.call('account.move', 'action_post', ids=[invoice_id])
            done.append('factura confirmada')

            invoice_context = self._context(
                active_model='account.move', active_ids=[invoice_id]
            )
            # El efectivo va al final y sin valor: así paga lo que falte, aunque Odoo
            # haya redondeado el total distinto por un centavo
            methods = sorted(amounts, key=lambda method: method == 'cash')
            for number, method in enumerate(methods, start=1):
                step = f'registrar el pago en {METHODS[method]}'
                vals = {'journal_id': self._journal(method)}
                if number < len(methods):
                    vals['amount'] = amounts[method]
                wizard = odoo.call(
                    'account.payment.register',
                    'create',
                    context=invoice_context,
                    vals_list=[vals],
                )[0]
                odoo.call(
                    'account.payment.register',
                    'action_create_payments',
                    ids=[wizard],
                    context=invoice_context,
                )
                done.append(f'pago en {METHODS[method]}')

            invoice = odoo.call(
                'account.move',
                'read',
                ids=[invoice_id],
                fields=['name', 'amount_total', 'payment_state'],
            )[0]
        except OdooError as error:
            already = f'\n\nYa quedó hecho en Odoo: {", ".join(done)}.' if done else ''
            raise SaleError(f'No se pudo {step}.\n\n{error}{already}') from None

        return SaleResult(
            order=order['name'],
            invoice=invoice['name'],
            total=invoice['amount_total'],
            payment_state=PAYMENT_STATES.get(
                invoice['payment_state'], invoice['payment_state']
            ),
        )
