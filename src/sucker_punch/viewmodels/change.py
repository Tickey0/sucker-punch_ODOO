from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QMessageBox

from ..models.customer import FINAL_CONSUMER_VAT, ID_TYPES, Customer
from ..models.payment import Payment
from ..services.customer_service import (
    FINAL_CONSUMER_LIMIT,
    CustomerService,
    check_contact,
    check_new_customer,
    guess_id_type,
    is_valid_cedula,
)
from ..services.odoo_client import OdooError
from ..views.ui_change import Ui_Change
from .theme import busy, set_state


class ChangeDialog(QDialog):
    """Cambio: Valor, Pagado y Cambio (vuelto), y el cliente de la factura.

    Enter en Identificación busca el cliente en Odoo: si existe, se llenan sus datos y el
    cursor salta a Guardar; si no existe, se escriben sus datos y se crea al guardar.
    ↑ ↓ moverse. Esc: volver a Pago Efectivo.
    """

    def __init__(
        self,
        payment: Payment,
        customers: CustomerService,
        limit_final_consumer: bool,
        customer: Customer | None = None,
        parent=None,
    ):
        super().__init__(parent)
        self.ui = Ui_Change()
        self.ui.setupUi(self)
        self.payment = payment
        self.customers = customers
        self.limit_final_consumer = limit_final_consumer  # regla del SRI en Ecuador
        self.customer: Customer | None = None  # el último buscado (o el nuevo)
        self.action = ''  # 'created' o 'updated' si al guardar se creó o corrigió
        ui = self.ui
        self.order = [
            ui.txt_identification,
            ui.cmb_id_type,
            ui.txt_name,
            ui.txt_email,
            ui.txt_street,
            ui.push_save,
            ui.push_cancel,
        ]
        for kind, label in ID_TYPES.items():
            ui.cmb_id_type.addItem(label, kind)

        big_font = QFont(self.font())
        big_font.setPointSize(int(self.font().pointSize() * 1.6))
        for label in (ui.lbl_value, ui.lbl_paid, ui.lbl_change, ui.lbl_change_title):
            label.setFont(big_font)
        ui.lbl_value.setText(f'{payment.total:.2f}')
        ui.lbl_paid.setText(f'{payment.paid:.2f}')
        ui.lbl_change.setText(f'{payment.change:.2f}')

        for widget in self.order:
            widget.installEventFilter(self)
        ui.txt_identification.textEdited.connect(self.identification_edited)
        ui.cmb_id_type.activated.connect(self.type_chosen)
        ui.push_save.clicked.connect(self.save)
        ui.push_cancel.clicked.connect(self.reject)

        if customer:
            self.show_customer(customer)
            self.check_final_consumer()
        else:
            ui.txt_identification.setText(FINAL_CONSUMER_VAT)
            self.lookup(move=False)
        ui.txt_identification.setFocus()
        ui.txt_identification.selectAll()

    # ---- Mensajes ----
    def show_message(self, text: str, state: str = ''):
        self.ui.lbl_status.setText(text)
        set_state(self.ui.lbl_status, state)

    def final_consumer_blocked(self, customer: Customer) -> bool:
        return (
            customer.is_final_consumer
            and self.limit_final_consumer
            and self.payment.total > FINAL_CONSUMER_LIMIT
        )

    def check_final_consumer(self) -> bool:
        """Avisa si la factura pasa del tope de Consumidor Final. True si se puede."""
        if self.customer and self.final_consumer_blocked(self.customer):
            self.show_message(
                f'La factura pasa de ${FINAL_CONSUMER_LIMIT:.2f}: el SRI no la deja a '
                'Consumidor Final. Escribe la cédula o RUC del cliente.',
                'error',
            )
            return False
        return True

    # ---- Cliente ----
    def show_customer(self, customer: Customer):
        self.customer = customer
        ui = self.ui
        ui.txt_identification.setText(customer.vat)
        ui.cmb_id_type.setCurrentIndex(ui.cmb_id_type.findData(customer.id_type))
        ui.txt_name.setText(customer.name)
        ui.txt_email.setText(customer.email)
        ui.txt_street.setText(customer.street)
        # Se pueden corregir y se actualizan en Odoo; el Consumidor Final no se toca
        for field in (ui.txt_name, ui.txt_email, ui.txt_street):
            field.setReadOnly(customer.is_final_consumer)

    def lookup(self, move: bool = True) -> bool:
        """Busca el cliente por la identificación. True si ya existe en Odoo."""
        ui = self.ui
        vat = ui.txt_identification.text().strip() or FINAL_CONSUMER_VAT
        try:
            with busy():
                if vat == FINAL_CONSUMER_VAT:
                    found = self.customers.final_consumer()
                else:
                    found = self.customers.find(vat)
        except OdooError as error:
            self.show_message(str(error), 'error')
            return False
        if found:
            self.show_customer(found)
            if self.check_final_consumer():
                self.show_message(f'✔ Cliente: {found.name}', 'ok')
                if move:
                    ui.push_save.setFocus()
            elif move:
                ui.txt_identification.selectAll()
            return True
        self.show_customer(Customer(vat=vat, id_type=guess_id_type(vat)))
        self.show_message(
            'Cliente nuevo: llena la Razón Social (email y dirección son opcionales). '
            'Se crea en Odoo al guardar.'
        )
        if move:
            ui.txt_name.setFocus()
        return False

    def identification_edited(self):
        ui = self.ui
        if self.customer and self.customer.id:
            # Los datos en pantalla eran de otro cliente
            for field in (ui.txt_name, ui.txt_email, ui.txt_street):
                field.clear()
                field.setReadOnly(False)
        self.customer = None
        self.show_message('Presiona Enter para buscar el cliente.')

    def type_chosen(self):
        ui = self.ui
        if ui.cmb_id_type.currentData() == 'final':
            ui.txt_identification.setText(FINAL_CONSUMER_VAT)
            self.lookup()
        elif ui.txt_identification.text().strip() == FINAL_CONSUMER_VAT:
            ui.txt_identification.clear()
            self.identification_edited()
            ui.txt_identification.setFocus()

    def form_customer(self) -> Customer:
        ui = self.ui
        return self.customer.model_copy(
            update={
                'id_type': ui.cmb_id_type.currentData(),
                'name': ui.txt_name.text().strip(),
                'email': ui.txt_email.text().strip(),
                'street': ui.txt_street.text().strip(),
            }
        )

    # ---- Guardar ----
    def save(self):
        ui = self.ui
        vat = ui.txt_identification.text().strip() or FINAL_CONSUMER_VAT
        if (self.customer is None or self.customer.vat != vat) and not self.lookup():
            return  # cliente nuevo: primero hay que llenar sus datos
        customer = self.form_customer()
        if not self.check_final_consumer():
            ui.txt_identification.setFocus()
            ui.txt_identification.selectAll()
            return

        if not customer.id:
            field, message = check_new_customer(customer)
            if message:
                self.show_message(message, 'error')
                widget = (
                    ui.txt_identification
                    if field == 'vat'
                    else getattr(ui, f'txt_{field}')
                )
                widget.setFocus()
                return
            if customer.id_type == 'cedula' and not is_valid_cedula(customer.vat):
                answer = QMessageBox.question(
                    self,
                    'Cédula',
                    f'La cédula {customer.vat} no cumple el dígito verificador.\n\n'
                    '¿Crear el cliente de todas formas?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No,
                )
                if answer != QMessageBox.StandardButton.Yes:
                    ui.txt_identification.setFocus()
                    return
            try:
                with busy():
                    customer = self.customers.create(customer)
            except OdooError as error:
                self.show_message(f'Odoo no creó el cliente: {error}', 'error')
                return
            self.action = 'created'
        elif changes := {
            field: getattr(customer, field)
            for field in ('name', 'email', 'street')
            if getattr(customer, field) != getattr(self.customer, field)
        }:
            field, message = check_contact(customer)
            if message:
                self.show_message(message, 'error')
                getattr(ui, f'txt_{field}').setFocus()
                return
            try:
                with busy():
                    self.customers.update(customer, changes)
            except OdooError as error:
                self.show_message(f'No se pudo actualizar el cliente: {error}', 'error')
                return
            self.action = 'updated'
        self.customer = customer
        self.accept()

    # ---- Teclado ----
    def move_focus(self, widget, step: int):
        """Al anterior o siguiente campo, saltando los que no se pueden editar."""
        position = self.order.index(widget) + step
        while 0 <= position < len(self.order):
            target = self.order[position]
            if not (hasattr(target, 'isReadOnly') and target.isReadOnly()):
                target.setFocus()
                if hasattr(target, 'selectAll'):
                    target.selectAll()
                return
            position += step

    def eventFilter(self, obj, event):
        if event.type() != QEvent.Type.KeyPress or obj not in self.order:
            return super().eventFilter(obj, event)
        ui, key = self.ui, event.key()
        if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if obj is ui.txt_identification:
                self.lookup()
            elif obj is ui.push_save:
                self.save()
            elif obj is ui.push_cancel:
                self.reject()
            elif obj is ui.txt_street:
                ui.push_save.setFocus()
            else:
                self.move_focus(obj, 1)
            return True  # Enter no llega al diálogo (no presiona otro botón)
        if key in (Qt.Key.Key_Up, Qt.Key.Key_Down) and obj is not ui.cmb_id_type:
            self.move_focus(obj, -1 if key == Qt.Key.Key_Up else 1)
            return True
        if key in (Qt.Key.Key_Left, Qt.Key.Key_Right) and obj in (
            ui.push_save,
            ui.push_cancel,
        ):
            (ui.push_cancel if obj is ui.push_save else ui.push_save).setFocus()
            return True
        return super().eventFilter(obj, event)
