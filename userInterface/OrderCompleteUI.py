from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

from util.get_resource_path import get_resource_path


class OrderCompleteUI(QWidget):
    def __init__(self, on_go_home):
        super().__init__()

        self.on_go_home = on_go_home

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        logo_label = QLabel()
        logo_pixmap = QPixmap(get_resource_path("assets/logo.png")).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        thank_you_label = QLabel("""
            <p style="line-height: 160%; font-size: 20px; font-weight: bold; text-align: center;">
                주문되었습니다.<br>
                오늘도 환경 보호에 동참해주셔서 감사합니다!
            </p>
        """)
        thank_you_label.setTextFormat(Qt.RichText)
        thank_you_label.setAlignment(Qt.AlignCenter)

        home_button = QPushButton("처음으로 돌아가기")
        home_button.setFixedSize(180, 40)
        home_button.clicked.connect(self.on_go_home)

        layout.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(thank_you_label)
        layout.addWidget(home_button, alignment=Qt.AlignBottom | Qt.AlignHCenter)

        self.setLayout(layout)
