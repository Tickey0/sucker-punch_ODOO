from PySide6.QtCore import QEvent, Qt, QTimer, Signal
from PySide6.QtWidgets import QLineEdit, QStyledItemDelegate


class BarcodeDelegate(QStyledItemDelegate):
    """Editor de la celda del código: convierte las teclas de la factura en acciones.

    Acciones: 'search' (Enter), 'save' (Ctrl+Enter), 'inventory' (F9), 'price' (F2),
    'delete' (Shift+F6), 'clear' (Ctrl+L), 'up', 'down'.
    """

    key_action = Signal(str, str)  # (acción, texto escrito)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setFrame(False)
        return editor

    def setEditorData(self, editor, index):
        editor.setText(str(index.data(Qt.ItemDataRole.EditRole) or ''))
        editor.selectAll()

    def setModelData(self, editor, model, index):
        # Al cerrar el editor solo la fila en blanco (la última) guarda lo escrito; las
        # demás siguen mostrando el código de su producto
        if index.row() == model.rowCount() - 1:
            model.setData(index, editor.text())

    def eventFilter(self, editor, event):
        if event.type() != QEvent.Type.KeyPress:
            return super().eventFilter(editor, event)
        key, modifiers = event.key(), event.modifiers()
        ctrl = modifiers & Qt.KeyboardModifier.ControlModifier
        # Ctrl+Enter y Ctrl+L también son atajos de la ventana; si llegan hasta aquí (la
        # ventana no estaba activa) se atienden igual
        if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            action = 'save' if ctrl else 'search'
        elif key == Qt.Key.Key_L and ctrl:
            action = 'clear'
        elif key == Qt.Key.Key_F9:
            action = 'inventory'
        elif key == Qt.Key.Key_F2:
            action = 'price'
        elif key == Qt.Key.Key_F6 and modifiers & Qt.KeyboardModifier.ShiftModifier:
            action = 'delete'
        elif key == Qt.Key.Key_Up:
            action = 'up'
        elif key == Qt.Key.Key_Down:
            action = 'down'
        elif key == Qt.Key.Key_Escape:
            editor.clear()
            return True
        elif key in (Qt.Key.Key_Tab, Qt.Key.Key_Backtab):
            return True  # el cursor no sale de la columna del código
        else:
            return super().eventFilter(editor, event)
        text = editor.text()
        # Se procesa después de soltar el evento: la tabla cambia y este editor se cierra
        QTimer.singleShot(0, lambda: self.key_action.emit(action, text))
        return True
