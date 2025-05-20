from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from PySide6.QtCore import Qt

CATEGORIES = ['아우터', '상의', '바지', '원피스/스커트', '신발', '악세사리']

class SelectCategoryUI(QWidget):
    def __init__(self, on_category_selected):
        super().__init__()
        self.on_category_selected = on_category_selected
        self.init_ui()

    def init_ui(self):
        outer_layout = QVBoxLayout()
        outer_layout.setAlignment(Qt.AlignCenter)

        inner_layout = QVBoxLayout()
        inner_layout.setAlignment(Qt.AlignCenter)

        title = QLabel("카테고리를 선택하세요")
        title.setObjectName("headerLabel")
        title.setAlignment(Qt.AlignCenter)
        inner_layout.addWidget(title)

        grid = QGridLayout()
        grid.setSpacing(20)
        grid.setAlignment(Qt.AlignCenter)

        for idx, category in enumerate(CATEGORIES):
            btn = QPushButton(category)
            btn.setFixedSize(150, 80)
            btn.clicked.connect(lambda _, c=category: self.on_category_selected(c))

            row = idx // 3
            col = idx % 3
            grid.addWidget(btn, row, col)

        inner_layout.addLayout(grid)
        outer_layout.addLayout(inner_layout)

        self.setLayout(outer_layout)
