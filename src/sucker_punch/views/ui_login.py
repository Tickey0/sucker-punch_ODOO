# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginiuFNjO.ui'
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
        self.lbl_user = QLabel(self.frameUser)
        self.lbl_user.setObjectName('lbl_user')
        self.lbl_user.setMaximumSize(QSize(180, 60))

        self.verticalLayout_2.addWidget(self.lbl_user)

        self.txt_user = QLineEdit(self.frameUser)
        self.txt_user.setObjectName('txt_user')

        self.verticalLayout_2.addWidget(self.txt_user)

        self.verticalLayout.addWidget(self.frameUser, 0, Qt.AlignmentFlag.AlignHCenter)

        self.framePassword = QFrame(Login)
        self.framePassword.setObjectName('framePassword')
        self.framePassword.setMinimumSize(QSize(300, 0))
        self.framePassword.setMaximumSize(QSize(16777215, 120))
        self.framePassword.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePassword.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.framePassword)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.lbl_password = QLabel(self.framePassword)
        self.lbl_password.setObjectName('lbl_password')
        self.lbl_password.setMaximumSize(QSize(180, 60))

        self.verticalLayout_3.addWidget(self.lbl_password)

        self.txt_password = QLineEdit(self.framePassword)
        self.txt_password.setObjectName('txt_password')
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_3.addWidget(self.txt_password)

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
        self.push_login = QPushButton(self.frameLogin)
        self.push_login.setObjectName('push_login')

        self.verticalLayout_4.addWidget(self.push_login)

        self.verticalLayout.addWidget(self.frameLogin, 0, Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate('Login', 'Dialog', None))
        self.lbl_user.setText(QCoreApplication.translate('Login', 'Usuario', None))
        self.lbl_password.setText(
            QCoreApplication.translate('Login', 'Contrase\u00f1a', None)
        )
        self.push_login.setText(QCoreApplication.translate('Login', 'Ingresar', None))

    # retranslateUi
