from PySide6.QtWidgets import QDialog, QMainWindow

from sucker_punch.viewmodels.login import Login

from ..views.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    username = 'user'
    password = 'secret'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_authenticated = self.try_login()

    def try_login(self) -> bool:
        while True:
            login = Login(self)
            if login.exec() != QDialog.DialogCode.Accepted:
                return False
            if login.user.name == self.username and login.user.password == self.password:
                return True
