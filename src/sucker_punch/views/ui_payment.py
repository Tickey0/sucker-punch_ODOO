# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payment.ui'
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
    QApplication,
    QDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Payment(object):
    def setupUi(self, Payment):
        if not Payment.objectName():
            Payment.setObjectName('Payment')
        Payment.resize(560, 420)
        Payment.setStyleSheet(
            'QDialog { background: white; }\n'
            'QFrame#frameAmounts { background: #fafafa; border: 1px solid #c8c8c8; border-radius: 4px; }\n'
            'QLabel#lbl_total { background: #e3f5e3; border: 1px solid #9ccc9c; border-radius: 4px;\n'
            '                   color: black; font-weight: bold; padding: 2px 10px; }\n'
            'QLabel#lbl_total_title { color: #000080; font-weight: bold; }\n'
            'QLineEdit { background: white; color: black; padding: 2px 6px;\n'
            '            selection-background-color: #1d4ed8; selection-color: white; }\n'
            'QLineEdit:focus { background: #ffff80; }\n'
            'QLabel#lbl_status[state="error"] { color: #b00020; font-weight: bold; }\n'
            'QLabel#lbl_status[state="ok"] { color: #006400; font-weight: bold; }\n'
            'QLabel#lbl_help { color: #707070; }'
        )
        self.verticalLayout = QVBoxLayout(Payment)
        self.verticalLayout.setObjectName('verticalLayout')
        self.frameAmounts = QFrame(Payment)
        self.frameAmounts.setObjectName('frameAmounts')
        self.frameAmounts.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout = QGridLayout(self.frameAmounts)
        self.gridLayout.setObjectName('gridLayout')
        self.lbl_total_title = QLabel(self.frameAmounts)
        self.lbl_total_title.setObjectName('lbl_total_title')

        self.gridLayout.addWidget(self.lbl_total_title, 0, 0, 1, 1)

        self.lbl_total = QLabel(self.frameAmounts)
        self.lbl_total.setObjectName('lbl_total')
        self.lbl_total.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_total, 0, 1, 1, 1)

        self.lbl_cash = QLabel(self.frameAmounts)
        self.lbl_cash.setObjectName('lbl_cash')

        self.gridLayout.addWidget(self.lbl_cash, 1, 0, 1, 1)

        self.txt_cash = QLineEdit(self.frameAmounts)
        self.txt_cash.setObjectName('txt_cash')
        self.txt_cash.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.txt_cash, 1, 1, 1, 1)

        self.lbl_card = QLabel(self.frameAmounts)
        self.lbl_card.setObjectName('lbl_card')

        self.gridLayout.addWidget(self.lbl_card, 2, 0, 1, 1)

        self.txt_card = QLineEdit(self.frameAmounts)
        self.txt_card.setObjectName('txt_card')
        self.txt_card.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.txt_card, 2, 1, 1, 1)

        self.lbl_transfer = QLabel(self.frameAmounts)
        self.lbl_transfer.setObjectName('lbl_transfer')

        self.gridLayout.addWidget(self.lbl_transfer, 3, 0, 1, 1)

        self.txt_transfer = QLineEdit(self.frameAmounts)
        self.txt_transfer.setObjectName('txt_transfer')
        self.txt_transfer.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.txt_transfer, 3, 1, 1, 1)

        self.lbl_other = QLabel(self.frameAmounts)
        self.lbl_other.setObjectName('lbl_other')

        self.gridLayout.addWidget(self.lbl_other, 4, 0, 1, 1)

        self.txt_other = QLineEdit(self.frameAmounts)
        self.txt_other.setObjectName('txt_other')
        self.txt_other.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.txt_other, 4, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.frameAmounts)

        self.lbl_status = QLabel(Payment)
        self.lbl_status.setObjectName('lbl_status')
        self.lbl_status.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_status)

        self.lbl_help = QLabel(Payment)
        self.lbl_help.setObjectName('lbl_help')
        self.lbl_help.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_help)

        self.verticalSpacer = QSpacerItem(
            20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frameButtons = QFrame(Payment)
        self.frameButtons.setObjectName('frameButtons')
        self.frameButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.push_accept = QPushButton(self.frameButtons)
        self.push_accept.setObjectName('push_accept')

        self.horizontalLayout.addWidget(self.push_accept)

        self.push_cancel = QPushButton(self.frameButtons)
        self.push_cancel.setObjectName('push_cancel')

        self.horizontalLayout.addWidget(self.push_cancel)

        self.verticalLayout.addWidget(self.frameButtons)

        QWidget.setTabOrder(self.txt_cash, self.txt_card)
        QWidget.setTabOrder(self.txt_card, self.txt_transfer)
        QWidget.setTabOrder(self.txt_transfer, self.txt_other)
        QWidget.setTabOrder(self.txt_other, self.push_accept)
        QWidget.setTabOrder(self.push_accept, self.push_cancel)

        self.retranslateUi(Payment)

        QMetaObject.connectSlotsByName(Payment)

    # setupUi

    def retranslateUi(self, Payment):
        Payment.setWindowTitle(
            QCoreApplication.translate('Payment', 'Pago Efectivo', None)
        )
        self.lbl_total_title.setText(
            QCoreApplication.translate('Payment', 'Pago Total', None)
        )
        self.lbl_total.setText(QCoreApplication.translate('Payment', '0.00', None))
        self.lbl_cash.setText(QCoreApplication.translate('Payment', 'Efectivo', None))
        self.txt_cash.setPlaceholderText(
            QCoreApplication.translate('Payment', '0.00', None)
        )
        self.lbl_card.setText(QCoreApplication.translate('Payment', 'Tarjeta', None))
        self.txt_card.setPlaceholderText(
            QCoreApplication.translate('Payment', '0.00', None)
        )
        self.lbl_transfer.setText(
            QCoreApplication.translate('Payment', 'Dep\u00f3sito / Transferencia', None)
        )
        self.txt_transfer.setPlaceholderText(
            QCoreApplication.translate('Payment', '0.00', None)
        )
        self.lbl_other.setText(QCoreApplication.translate('Payment', 'Otros', None))
        self.txt_other.setPlaceholderText(
            QCoreApplication.translate('Payment', '0.00', None)
        )
        self.lbl_status.setText('')
        self.lbl_help.setText(
            QCoreApplication.translate(
                'Payment',
                'Enter: siguiente (si ya alcanza, pasa a Cambio)    \u2191 \u2193: moverse    Esc: volver a la factura',
                None,
            )
        )
        self.push_accept.setText(
            QCoreApplication.translate('Payment', 'Aceptar  (Enter)', None)
        )
        self.push_cancel.setText(
            QCoreApplication.translate('Payment', '\u2716  Cancelar  (Esc)', None)
        )

    # retranslateUi
