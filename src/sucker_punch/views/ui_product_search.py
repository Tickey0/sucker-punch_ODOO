# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_search.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QDialog,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_ProductSearch(object):
    def setupUi(self, ProductSearch):
        if not ProductSearch.objectName():
            ProductSearch.setObjectName('ProductSearch')
        ProductSearch.resize(860, 480)
        ProductSearch.setStyleSheet(
            'QTableWidget { background: white; color: black; gridline-color: #dcdcdc; }\n'
            'QTableWidget::item:selected { background: #e6ff8c; color: black; }\n'
            'QHeaderView::section { background: #f4f6fb; color: #000080; font-weight: bold;\n'
            '                       border: none; border-bottom: 2px solid #000080; padding: 4px; }'
        )
        self.verticalLayout = QVBoxLayout(ProductSearch)
        self.verticalLayout.setObjectName('verticalLayout')
        self.frameSearch = QFrame(ProductSearch)
        self.frameSearch.setObjectName('frameSearch')
        self.frameSearch.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameSearch)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.lbl_search = QLabel(self.frameSearch)
        self.lbl_search.setObjectName('lbl_search')

        self.horizontalLayout.addWidget(self.lbl_search)

        self.txt_search = QLineEdit(self.frameSearch)
        self.txt_search.setObjectName('txt_search')

        self.horizontalLayout.addWidget(self.txt_search)

        self.verticalLayout.addWidget(self.frameSearch)

        self.table_products = QTableWidget(ProductSearch)
        if self.table_products.columnCount() < 4:
            self.table_products.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_products.setObjectName('table_products')
        self.table_products.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_products.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.table_products.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_products.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_products)

        self.lbl_status = QLabel(ProductSearch)
        self.lbl_status.setObjectName('lbl_status')

        self.verticalLayout.addWidget(self.lbl_status)

        self.frameButtons = QFrame(ProductSearch)
        self.frameButtons.setObjectName('frameButtons')
        self.frameButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frameButtons)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.push_search = QPushButton(self.frameButtons)
        self.push_search.setObjectName('push_search')
        self.push_search.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.push_search)

        self.push_accept = QPushButton(self.frameButtons)
        self.push_accept.setObjectName('push_accept')
        self.push_accept.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.push_accept)

        self.push_cancel = QPushButton(self.frameButtons)
        self.push_cancel.setObjectName('push_cancel')
        self.push_cancel.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.push_cancel)

        self.verticalLayout.addWidget(self.frameButtons)

        self.retranslateUi(ProductSearch)

        QMetaObject.connectSlotsByName(ProductSearch)

    # setupUi

    def retranslateUi(self, ProductSearch):
        ProductSearch.setWindowTitle(
            QCoreApplication.translate('ProductSearch', 'Maestro de Art\u00edculos', None)
        )
        self.lbl_search.setText(
            QCoreApplication.translate('ProductSearch', 'Buscar', None)
        )
        self.txt_search.setPlaceholderText(
            QCoreApplication.translate(
                'ProductSearch',
                'Nombre o c\u00f3digo. % es comod\u00edn: CHOCOL% = empieza con CHOCOL',
                None,
            )
        )
        ___qtablewidgetitem = self.table_products.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate('ProductSearch', 'Nombre Art\u00edculo', None)
        )
        ___qtablewidgetitem1 = self.table_products.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate('ProductSearch', 'Precio Venta', None)
        )
        ___qtablewidgetitem2 = self.table_products.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate('ProductSearch', 'C\u00f3digo Barras', None)
        )
        ___qtablewidgetitem3 = self.table_products.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate('ProductSearch', 'Stock', None)
        )
        self.lbl_status.setText('')
        self.push_search.setText(
            QCoreApplication.translate('ProductSearch', 'Buscar', None)
        )
        self.push_accept.setText(
            QCoreApplication.translate('ProductSearch', 'Aceptar', None)
        )
        self.push_cancel.setText(
            QCoreApplication.translate('ProductSearch', 'Cancelar', None)
        )

    # retranslateUi
