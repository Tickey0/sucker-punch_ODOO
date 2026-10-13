from PySide6.QtWidgets import QDialog

from ..models.user import User
from ..views.ui_login import Ui_Login


class Login(QDialog):
    user: User

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.push_login.clicked.connect(self.accept_action)
        self.user = User(name='', password='')

    def accept_action(self):
        self.user = User(
            name=self.ui.txt_user.text(), password=self.ui.txt_password.text()
        )
        self.accept()
