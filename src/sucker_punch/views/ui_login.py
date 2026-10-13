# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginQCBlkF.ui'
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
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName('Login')
        Login.resize(418, 243)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName('verticalLayout')
        self.frameUser = QFrame(Login)
        self.frameUser.setObjectName('frameUser')
        self.frameUser.setMinimumSize(QSize(300, 0))
        self.frameUser.setMaximumSize(QSize(16777215, 120))
        self.frameUser.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameUser.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameUser)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.lblUser = QLabel(self.frameUser)
        self.lblUser.setObjectName('lblUser')
        self.lblUser.setMaximumSize(QSize(180, 60))

        self.verticalLayout_2.addWidget(self.lblUser)

        self.txtUser = QLineEdit(self.frameUser)
        self.txtUser.setObjectName('txtUser')

        self.verticalLayout_2.addWidget(self.txtUser)

        self.verticalLayout.addWidget(self.frameUser, 0, Qt.AlignmentFlag.AlignHCenter)

        self.framePassword = QFrame(Login)
        self.framePassword.setObjectName('framePassword')
        self.framePassword.setMinimumSize(QSize(300, 0))
        self.framePassword.setMaximumSize(QSize(16777215, 120))
        self.framePassword.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePassword.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.framePassword)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.lblPassword = QLabel(self.framePassword)
        self.lblPassword.setObjectName('lblPassword')
        self.lblPassword.setMaximumSize(QSize(180, 60))

        self.verticalLayout_3.addWidget(self.lblPassword)

        self.txtPassword = QLineEdit(self.framePassword)
        self.txtPassword.setObjectName('txtPassword')
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_3.addWidget(self.txtPassword)

        self.verticalLayout.addWidget(
            self.framePassword, 0, Qt.AlignmentFlag.AlignHCenter
        )

        self.frameLogin = QFrame(Login)
        self.frameLogin.setObjectName('frameLogin')
        self.frameLogin.setMinimumSize(QSize(180, 0))
        self.frameLogin.setMaximumSize(QSize(600, 60))
        self.frameLogin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogin.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameLogin)
        self.verticalLayout_4.setObjectName('verticalLayout_4')
        self.pushLogin = QPushButton(self.frameLogin)
        self.pushLogin.setObjectName('pushLogin')

        self.verticalLayout_4.addWidget(self.pushLogin)

        self.verticalLayout.addWidget(self.frameLogin, 0, Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate('Login', 'Dialog', None))
        self.lblUser.setText(QCoreApplication.translate('Login', 'Usuario', None))
        self.lblPassword.setText(
            QCoreApplication.translate('Login', 'Contrase\u00f1a', None)
        )
        self.pushLogin.setText(QCoreApplication.translate('Login', 'Ingresar', None))

    # retranslateUi
