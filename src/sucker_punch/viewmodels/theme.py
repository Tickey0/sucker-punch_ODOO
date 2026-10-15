import ctypes
import sys
from contextlib import contextmanager
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QIcon, QPalette
from PySide6.QtWidgets import QApplication, QWidget

ICON = Path(__file__).resolve().parents[1] / 'assets' / 'images' / 'icon.png'


def apply_icon(app: QApplication):
    """Ícono de la app en todas las ventanas y en la barra de tareas."""
    if sys.platform == 'win32':
        # Sin esto Windows agrupa la app con python.exe y muestra el ícono de Python
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('sucker-punch')
    app.setWindowIcon(QIcon(str(ICON)))


@contextmanager
def busy():
    """Reloj de espera mientras se habla con Odoo."""
    QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
    try:
        yield
    finally:
        QApplication.restoreOverrideCursor()


def set_state(widget: QWidget, state: str):
    """Cambia la propiedad «state» (ej. error / ok) que usan los styleSheet de los .ui."""
    widget.setProperty('state', state)
    widget.style().unpolish(widget)
    widget.style().polish(widget)


def apply_theme(app: QApplication):
    """Siempre en modo claro: con Windows en modo oscuro las tablas salían azul marino."""
    app.setStyle('Fusion')
    app.styleHints().setColorScheme(Qt.ColorScheme.Light)
    palette = QPalette()
    for role, color in (
        (QPalette.ColorRole.Window, 'white'),
        (QPalette.ColorRole.WindowText, 'black'),
        (QPalette.ColorRole.Base, 'white'),
        (QPalette.ColorRole.AlternateBase, 'white'),
        (QPalette.ColorRole.Text, 'black'),
        (QPalette.ColorRole.Button, '#f0f0f0'),
        (QPalette.ColorRole.ButtonText, 'black'),
        (QPalette.ColorRole.Highlight, '#e6ff8c'),
        (QPalette.ColorRole.HighlightedText, 'black'),
        (QPalette.ColorRole.ToolTipBase, '#ffffe1'),
        (QPalette.ColorRole.ToolTipText, 'black'),
    ):
        palette.setColor(role, QColor(color))
    # Lo bloqueado (ej.: un dato que viene del sistema en Configuración) se ve gris
    for role, color in (
        (QPalette.ColorRole.Base, '#f0f0f0'),
        (QPalette.ColorRole.Text, '#808080'),
        (QPalette.ColorRole.WindowText, '#808080'),
        (QPalette.ColorRole.ButtonText, '#808080'),
    ):
        palette.setColor(QPalette.ColorGroup.Disabled, role, QColor(color))
    app.setPalette(palette)


def apply_font_size(size: int):
    """Tamaño de letra de toda la app (Configuración → Tamaño de letra)."""
    font = QFont(QApplication.font())
    font.setPointSize(size)
    QApplication.setFont(font)
