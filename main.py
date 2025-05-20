import sys

from PySide6.QtWidgets import QApplication

from apply_global_theme import apply_global_theme
from userInterface.MainAppWindow import MainAppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainAppWindow()
    window.show()

    apply_global_theme(app)
    sys.exit(app.exec())
