import sys

from PySide6.QtWidgets import QApplication

from .views.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    widget = MainWindow()
    if not widget.is_authenticated:
        return
    widget.show()
    sys.exit(app.exec())
