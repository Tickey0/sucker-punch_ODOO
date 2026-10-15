import sys

from PySide6.QtWidgets import QApplication

from .services.settings_service import SettingsService
from .viewmodels.main_window import MainWindow
from .viewmodels.theme import apply_font_size, apply_icon, apply_theme


def main() -> None:
    app = QApplication(sys.argv)
    apply_theme(app)
    apply_icon(app)
    apply_font_size(SettingsService().load().font_size)
    widget = MainWindow()
    if not widget.is_authenticated:
        return
    widget.show()
    sys.exit(app.exec())
