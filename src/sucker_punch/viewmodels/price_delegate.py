from PySide6.QtCore import QEvent, QRegularExpression, Qt, QTimer, Signal
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QLineEdit, QStyledItemDelegate


class PriceDelegate(QStyledItemDelegate):
    """Editor del precio unitario (F2). Enter lo cambia; Esc lo deja como estaba."""

    price_entered = Signal(int, float)  # (fila, precio nuevo)
    cancelled = Signal(int)  # fila

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setFrame(False)
        editor.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        # Hasta 4 decimales, con punto o coma
        editor.setValidator(
            QRegularExpressionValidator(QRegularExpression(r'^\d{0,7}([.,]\d{0,4})?$'))
        )
        editor.setProperty('row', index.row())
        return editor

    def setEditorData(self, editor, index):
        editor.setText(str(index.data(Qt.ItemDataRole.EditRole) or ''))
        editor.selectAll()

    def setModelData(self, editor, model, index):
        pass  # el punto de venta cambia el precio de la línea y la vuelve a calcular

    def eventFilter(self, editor, event):
        if event.type() != QEvent.Type.KeyPress:
            return super().eventFilter(editor, event)
        key, row = event.key(), editor.property('row')
        if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            text = editor.text().replace(',', '.')
            if not text.strip('.'):
                return True  # vacío: sigue esperando el precio
            price = float(text)
            QTimer.singleShot(0, lambda: self.price_entered.emit(row, price))
            return True
        if key == Qt.Key.Key_Escape:
            QTimer.singleShot(0, lambda: self.cancelled.emit(row))
            return True
        if key in (Qt.Key.Key_Up, Qt.Key.Key_Down, Qt.Key.Key_Tab, Qt.Key.Key_Backtab):
            return True  # se termina con Enter o Esc
        return super().eventFilter(editor, event)
