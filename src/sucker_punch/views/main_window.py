from PySide6.QtWidgets import QDialog, QMainWindow, QMessageBox

from sucker_punch.views.login import Login

from .ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    user = 'user'
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
            if login.user == self.user and login.password == self.password:
                return True

