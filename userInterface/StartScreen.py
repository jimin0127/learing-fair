from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt


class StartScreen(QWidget):
    def __init__(self, on_start_clicked):
        super().__init__()
        self.on_start_clicked = on_start_clicked
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        logo_label = QLabel()
        pixmap = QPixmap("assets/logo.png").scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel("헌옷줄게 새옷다오")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)

        start_btn = QPushButton("시작하기")
        start_btn.setFixedSize(160, 40)
        start_btn.clicked.connect(self.on_start_clicked)

        layout.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(title_label)
        layout.addWidget(start_btn, alignment=Qt.AlignBottom | Qt.AlignHCenter)

        self.setLayout(layout)
