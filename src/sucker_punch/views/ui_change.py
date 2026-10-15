# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change.ui'
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
    QComboBox,
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


class Ui_Change(object):
    def setupUi(self, Change):
        if not Change.objectName():
            Change.setObjectName('Change')
        Change.resize(620, 560)
        Change.setStyleSheet(
            'QDialog { background: white; }\n'
            'QFrame#frameAmounts, QFrame#frameCustomer { background: #fafafa; border: 1px solid #c8c8c8;\n'
            '                                            border-radius: 4px; }\n'
            'QLabel#lbl_value, QLabel#lbl_paid, QLabel#lbl_change { border: 1px solid #a0a0a0;\n'
            '                                                      color: black; padding: 2px 12px; }\n'
            'QLabel#lbl_value { background: #ffffb0; }\n'
            'QLabel#lbl_paid { background: #c8f5ff; }\n'
            'QLabel#lbl_change { background: #c8f5c8; font-weight: bold; }\n'
            'QLabel#lbl_change_title { font-weight: bold; }\n'
            'QLineEdit, QComboBox { background: white; color: black; padding: 2px 6px; }\n'
            'QLineEdit:focus, QComboBox:focus { background: #ffff80; }\n'
            'QLineEdit:read-only { background: #f0f0f0; color: #404040; }\n'
            'QPushButton#push_save, QPushButton#push_cancel { background: #f4f6fb; color: #000080;\n'
            '    border: 1px solid #000080; border-radius: 4px; padding: 8px 18px; font-weight: bold; }\n'
            'QPushButton#push_save:focus, QPushButton#push'
            '_cancel:focus { background: #e6ff8c; }\n'
            'QLabel#lbl_status[state="error"] { color: #b00020; font-weight: bold; }\n'
            'QLabel#lbl_status[state="ok"] { color: #006400; font-weight: bold; }\n'
            'QLabel#lbl_help { color: #707070; }'
        )
        self.verticalLayout = QVBoxLayout(Change)
        self.verticalLayout.setObjectName('verticalLayout')
        self.frameAmounts = QFrame(Change)
        self.frameAmounts.setObjectName('frameAmounts')
        self.frameAmounts.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout = QGridLayout(self.frameAmounts)
        self.gridLayout.setObjectName('gridLayout')
        self.lbl_value_title = QLabel(self.frameAmounts)
        self.lbl_value_title.setObjectName('lbl_value_title')
        self.lbl_value_title.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_value_title, 0, 0, 1, 1)

        self.lbl_value = QLabel(self.frameAmounts)
        self.lbl_value.setObjectName('lbl_value')
        self.lbl_value.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_value, 0, 1, 1, 1)

        self.lbl_paid_title = QLabel(self.frameAmounts)
        self.lbl_paid_title.setObjectName('lbl_paid_title')
        self.lbl_paid_title.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_paid_title, 1, 0, 1, 1)

        self.lbl_paid = QLabel(self.frameAmounts)
        self.lbl_paid.setObjectName('lbl_paid')
        self.lbl_paid.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_paid, 1, 1, 1, 1)

        self.lbl_change_title = QLabel(self.frameAmounts)
        self.lbl_change_title.setObjectName('lbl_change_title')
        self.lbl_change_title.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_change_title, 2, 0, 1, 1)

        self.lbl_change = QLabel(self.frameAmounts)
        self.lbl_change.setObjectName('lbl_change')
        self.lbl_change.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.lbl_change, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.frameAmounts)

        self.frameButtons = QFrame(Change)
        self.frameButtons.setObjectName('frameButtons')
        self.frameButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.push_save = QPushButton(self.frameButtons)
        self.push_save.setObjectName('push_save')

        self.horizontalLayout.addWidget(self.push_save)

        self.push_cancel = QPushButton(self.frameButtons)
        self.push_cancel.setObjectName('push_cancel')

        self.horizontalLayout.addWidget(self.push_cancel)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.frameButtons)

        self.frameCustomer = QFrame(Change)
        self.frameCustomer.setObjectName('frameCustomer')
        self.frameCustomer.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout_2 = QGridLayout(self.frameCustomer)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.gridLayout_2.setVerticalSpacing(8)
        self.lbl_identification = QLabel(self.frameCustomer)
        self.lbl_identification.setObjectName('lbl_identification')

        self.gridLayout_2.addWidget(self.lbl_identification, 0, 0, 1, 1)

        self.txt_identification = QLineEdit(self.frameCustomer)
        self.txt_identification.setObjectName('txt_identification')
        self.txt_identification.setMaxLength(20)

        self.gridLayout_2.addWidget(self.txt_identification, 0, 1, 1, 1)

        self.lbl_id_type = QLabel(self.frameCustomer)
        self.lbl_id_type.setObjectName('lbl_id_type')

        self.gridLayout_2.addWidget(self.lbl_id_type, 1, 0, 1, 1)

        self.cmb_id_type = QComboBox(self.frameCustomer)
        self.cmb_id_type.setObjectName('cmb_id_type')

        self.gridLayout_2.addWidget(self.cmb_id_type, 1, 1, 1, 1)

        self.lbl_name = QLabel(self.frameCustomer)
        self.lbl_name.setObjectName('lbl_name')

        self.gridLayout_2.addWidget(self.lbl_name, 2, 0, 1, 1)

        self.txt_name = QLineEdit(self.frameCustomer)
        self.txt_name.setObjectName('txt_name')

        self.gridLayout_2.addWidget(self.txt_name, 2, 1, 1, 1)

        self.lbl_email = QLabel(self.frameCustomer)
        self.lbl_email.setObjectName('lbl_email')

        self.gridLayout_2.addWidget(self.lbl_email, 3, 0, 1, 1)

        self.txt_email = QLineEdit(self.frameCustomer)
        self.txt_email.setObjectName('txt_email')

        self.gridLayout_2.addWidget(self.txt_email, 3, 1, 1, 1)

        self.lbl_street = QLabel(self.frameCustomer)
        self.lbl_street.setObjectName('lbl_street')

        self.gridLayout_2.addWidget(self.lbl_street, 4, 0, 1, 1)

        self.txt_street = QLineEdit(self.frameCustomer)
        self.txt_street.setObjectName('txt_street')

        self.gridLayout_2.addWidget(self.txt_street, 4, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.frameCustomer)

        self.lbl_status = QLabel(Change)
        self.lbl_status.setObjectName('lbl_status')
        self.lbl_status.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_status)

        self.lbl_help = QLabel(Change)
        self.lbl_help.setObjectName('lbl_help')
        self.lbl_help.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_help)

        QWidget.setTabOrder(self.txt_identification, self.cmb_id_type)
        QWidget.setTabOrder(self.cmb_id_type, self.txt_name)
        QWidget.setTabOrder(self.txt_name, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_street)
        QWidget.setTabOrder(self.txt_street, self.push_save)
        QWidget.setTabOrder(self.push_save, self.push_cancel)

        self.retranslateUi(Change)

        QMetaObject.connectSlotsByName(Change)

    # setupUi

    def retranslateUi(self, Change):
        Change.setWindowTitle(QCoreApplication.translate('Change', 'Cambio', None))
        self.lbl_value_title.setText(QCoreApplication.translate('Change', 'Valor', None))
        self.lbl_value.setText(QCoreApplication.translate('Change', '0.00', None))
        self.lbl_paid_title.setText(QCoreApplication.translate('Change', 'Pagado', None))
        self.lbl_paid.setText(QCoreApplication.translate('Change', '0.00', None))
        self.lbl_change_title.setText(
            QCoreApplication.translate('Change', 'Cambio', None)
        )
        self.lbl_change.setText(QCoreApplication.translate('Change', '0.00', None))
        self.push_save.setText(
            QCoreApplication.translate('Change', '\U0001f4be  Guardar', None)
        )
        self.push_cancel.setText(
            QCoreApplication.translate('Change', '\u2716  Cancelar', None)
        )
        self.lbl_identification.setText(
            QCoreApplication.translate('Change', 'Identificaci\u00f3n', None)
        )
        self.txt_identification.setPlaceholderText(
            QCoreApplication.translate(
                'Change', 'C\u00e9dula, RUC o pasaporte + Enter', None
            )
        )
        self.lbl_id_type.setText(QCoreApplication.translate('Change', 'Tipo', None))
        self.lbl_name.setText(
            QCoreApplication.translate('Change', 'Raz\u00f3n Social', None)
        )
        self.lbl_email.setText(QCoreApplication.translate('Change', 'Email', None))
        self.lbl_street.setText(
            QCoreApplication.translate('Change', 'Direcci\u00f3n', None)
        )
        self.lbl_status.setText('')
        self.lbl_help.setText(
            QCoreApplication.translate(
                'Change',
                'Enter en Identificaci\u00f3n: buscar el cliente    \u2191 \u2193: moverse    Esc: volver a Pago Efectivo',
                None,
            )
        )

    # retranslateUi
