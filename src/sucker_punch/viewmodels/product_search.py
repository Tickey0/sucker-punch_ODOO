from PySide6.QtCore import QEvent, Qt
from PySide6.QtWidgets import QDialog, QHeaderView, QMessageBox, QTableWidgetItem

from ..models.product import Product
from ..services.odoo_client import OdooError
from ..services.product_service import ProductService
from ..views.ui_product_search import Ui_ProductSearch


class ProductSearch(QDialog):
    """Maestro de Artículos (F9): busca en el inventario de Odoo y devuelve el elegido.

    Enter en "Buscar" busca; flechas recorren la lista; Enter en la lista acepta; Esc
    cancela.
    """

    def __init__(
        self,
        products: ProductService,
        pattern: str,
        results: list[Product] | None = None,
        parent=None,
    ):
        super().__init__(parent)
        self.ui = Ui_ProductSearch()
        self.ui.setupUi(self)
        self.products = products
        self.results: list[Product] = []
        self.selected: Product | None = None

        header = self.ui.table_products.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        for column in (1, 2, 3):
            header.setSectionResizeMode(column, QHeaderView.ResizeMode.ResizeToContents)

        self.ui.txt_search.setText(pattern)
        self.ui.txt_search.installEventFilter(self)
        self.ui.table_products.installEventFilter(self)
        self.ui.table_products.doubleClicked.connect(self.accept_selected)
        self.ui.push_search.clicked.connect(self.search)
        self.ui.push_accept.clicked.connect(self.accept_selected)
        self.ui.push_cancel.clicked.connect(self.reject)

        if results is None:
            self.search()
        else:
            self.show_results(results)

    def search(self):
        pattern = self.ui.txt_search.text().strip() or '%'
        try:
            self.show_results(self.products.search(pattern))
        except OdooError as error:
            QMessageBox.critical(self, 'Error', str(error))

    def show_results(self, results: list[Product]):
        self.results = results
        table = self.ui.table_products
        table.setRowCount(len(results))
        for row, product in enumerate(results):
            for column, (text, alignment) in enumerate(
                (
                    (product.name, Qt.AlignmentFlag.AlignLeft),
                    (f'{product.price:.2f}', Qt.AlignmentFlag.AlignRight),
                    (product.code, Qt.AlignmentFlag.AlignLeft),
                    (f'{product.stock:g}', Qt.AlignmentFlag.AlignRight),
                )
            ):
                item = QTableWidgetItem(text)
                item.setTextAlignment(alignment | Qt.AlignmentFlag.AlignVCenter)
                table.setItem(row, column, item)
        if results:
            self.ui.lbl_status.setText(f'{len(results)} artículo(s)')
            table.selectRow(0)
            table.setFocus()
        else:
            self.ui.lbl_status.setText('No hay artículos con ese texto')
            self.ui.txt_search.setFocus()
            self.ui.txt_search.selectAll()

    def accept_selected(self):
        row = self.ui.table_products.currentRow()
        if 0 <= row < len(self.results):
            self.selected = self.results[row]
            self.accept()

    def eventFilter(self, obj, event):
        if event.type() != QEvent.Type.KeyPress:
            return False
        key = event.key()
        if obj is self.ui.txt_search:
            if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                self.search()
                return True
            if key == Qt.Key.Key_Down and self.results:
                self.ui.table_products.setFocus()
                return True
        elif obj is self.ui.table_products and key in (
            Qt.Key.Key_Return,
            Qt.Key.Key_Enter,
        ):
            self.accept_selected()
            return True
        return False
