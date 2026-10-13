# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog

from .ui_login import Ui_Login


class Login(QDialog):
    user = ''
    password = ''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushLogin.clicked.connect(self.accept_action)

    def accept_action(self):
        self.user = self.ui.txtUser.text()
        self.password = self.ui.txtPassword.text()
        self.accept()