from PySide6.QtCore import QEvent, QRegularExpression, Qt
from PySide6.QtGui import QFont, QRegularExpressionValidator
from PySide6.QtWidgets import QDialog

from ..models.payment import Payment
from ..views.ui_payment import Ui_Payment
from .theme import set_state


def to_amount(text: str) -> float:
    text = text.strip().replace(',', '.')
    return round(float(text), 2) if text.strip('.') else 0.0


class PaymentDialog(QDialog):
    """Pago Efectivo: cuánto paga el cliente con cada forma de pago.

    Enter: si ya alcanza, pasa a Cambio; si falta, salta a la siguiente forma de pago
    con lo que falta. ↑ ↓ moverse. Esc: volver a la factura.
    """

    def __init__(self, payment: Payment, parent=None):
        super().__init__(parent)
        self.ui = Ui_Payment()
        self.ui.setupUi(self)
        self.payment = payment
        self.fields = {
            'cash': self.ui.txt_cash,
            'card': self.ui.txt_card,
            'transfer': self.ui.txt_transfer,
            'other': self.ui.txt_other,
        }
        validator = QRegularExpressionValidator(
            QRegularExpression(r'^\d{0,7}([.,]\d{0,2})?$'), self
        )
        for method, field in self.fields.items():
            amount = getattr(payment, method)
            field.setText(f'{amount:.2f}' if amount else '')
            field.setValidator(validator)
            field.installEventFilter(self)
            field.textChanged.connect(self.update_status)

        total_font = QFont(self.font())
        total_font.setPointSize(int(self.font().pointSize() * 1.6))
        total_font.setBold(True)
        self.ui.lbl_total.setFont(total_font)
        self.ui.lbl_total.setText(f'{payment.total:.2f}')

        self.ui.push_accept.clicked.connect(self.accept_payment)
        self.ui.push_cancel.clicked.connect(self.reject)
        self.update_status()
        self.ui.txt_cash.setFocus()
        self.ui.txt_cash.selectAll()

    def form_payment(self) -> Payment:
        return Payment(
            total=self.payment.total,
            **{method: to_amount(field.text()) for method, field in self.fields.items()},
        )

    def problem(self, payment: Payment) -> str:
        if payment.non_cash > payment.total:
            return (
                'Tarjeta, depósito y otros no pueden pasar del total: el vuelto sale '
                'solo del efectivo.'
            )
        if payment.missing:
            return f'Falta ${payment.missing:.2f}'
        return ''

    def update_status(self):
        payment = self.form_payment()
        problem = self.problem(payment)
        if problem:
            self.ui.lbl_status.setText(problem)
            set_state(self.ui.lbl_status, 'error')
        else:
            change = f'Vuelto ${payment.change:.2f}' if payment.change else 'Pago exacto'
            self.ui.lbl_status.setText(f'✔ {change}')
            set_state(self.ui.lbl_status, 'ok')

    def accept_payment(self):
        payment = self.form_payment()
        if self.problem(payment):
            self.ui.txt_cash.setFocus()
            self.ui.txt_cash.selectAll()
            return
        self.payment = payment
        self.accept()

    def go_to_field(self, field):
        field.setFocus()
        field.selectAll()

    def eventFilter(self, obj, event):
        if event.type() != QEvent.Type.KeyPress or obj not in self.fields.values():
            return super().eventFilter(obj, event)
        fields = list(self.fields.values())
        position = fields.index(obj)
        key = event.key()
        if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            payment = self.form_payment()
            if not self.problem(payment):
                self.accept_payment()
            elif payment.non_cash <= payment.total and position < len(fields) - 1:
                # Falta: la siguiente forma de pago arranca con lo que falta
                following = fields[position + 1]
                if not to_amount(following.text()):
                    following.setText(f'{payment.missing:.2f}')
                self.go_to_field(following)
            return True  # Enter no llega al diálogo (no presiona otro botón)
        if key == Qt.Key.Key_Up and position > 0:
            self.go_to_field(fields[position - 1])
            return True
        if key == Qt.Key.Key_Down and position < len(fields) - 1:
            self.go_to_field(fields[position + 1])
            return True
        return super().eventFilter(obj, event)
