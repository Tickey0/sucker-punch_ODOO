from pydantic import BaseModel

# Forma de pago → texto en la pantalla Pago Efectivo
METHODS = {
    'cash': 'Efectivo',
    'card': 'Tarjeta',
    'transfer': 'Depósito / Transferencia',
    'other': 'Otros',
}


class Payment(BaseModel):
    """Cómo paga el cliente la factura: un valor por cada forma de pago."""

    total: float  # valor de la factura
    cash: float = 0.0
    card: float = 0.0
    transfer: float = 0.0
    other: float = 0.0

    @property
    def paid(self) -> float:
        return round(self.cash + self.card + self.transfer + self.other, 2)

    @property
    def non_cash(self) -> float:
        return round(self.card + self.transfer + self.other, 2)

    @property
    def missing(self) -> float:
        return round(max(0.0, self.total - self.paid), 2)

    @property
    def change(self) -> float:
        """Vuelto. Solo se da del efectivo: tarjeta, depósito y otros van exactos."""
        return round(max(0.0, self.paid - self.total), 2)

    def amounts(self) -> dict[str, float]:
        """Lo que se registra en Odoo por cada forma de pago (efectivo sin el vuelto)."""
        values = {
            'card': self.card,
            'transfer': self.transfer,
            'other': self.other,
            'cash': round(self.cash - self.change, 2),
        }
        return {method: amount for method, amount in values.items() if amount > 0}
