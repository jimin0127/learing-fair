from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QGridLayout, \
    QScrollArea
from PySide6.QtCore import Qt

from service.ProductService import ProductService
from util.format_price import format_price
from util.get_resource_path import get_resource_path


class ProductItem(QWidget):
    def __init__(self, product, open_product_detail):
        super().__init__()
        self.product = product
        self.open_product_detail = open_product_detail

        card_frame = QFrame()
        card_frame.setFixedHeight(280)

        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(get_resource_path(product["image_path"])).scaled(120, 120, Qt.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        name_label = QLabel(product["name"])
        name_label.setObjectName("headerLabel")
        name_label.setWordWrap(True)
        price_label = QLabel(format_price(product['price']))
        brand_label = QLabel(product["brand"])
        name_label.setAlignment(Qt.AlignCenter)
        price_label.setAlignment(Qt.AlignCenter)
        brand_label.setAlignment(Qt.AlignCenter)

        action_layout = QHBoxLayout()
        buy_btn = QPushButton("구매하기")
        buy_btn.setFixedSize(180, 30)
        buy_btn.clicked.connect(lambda: open_product_detail(self.product))
        action_layout.addWidget(buy_btn)

        card_layout.addWidget(image_label)
        card_layout.addWidget(brand_label)
        card_layout.addWidget(name_label)
        card_layout.addWidget(price_label)
        card_layout.addLayout(action_layout)
        card_frame.setLayout(card_layout)

        outer_layout = QVBoxLayout()
        outer_layout.addWidget(card_frame)
        self.setLayout(outer_layout)

class SelectProductUI(QWidget):
    def __init__(self, open_product_detail, selected_category, on_back):
        super().__init__()
        self.product_service = ProductService()
        self.selected_category = selected_category
        self.on_back = on_back
        products = self.product_service.find_all_by_category(selected_category)

        top_bar_layout = QGridLayout()

        top_bar_layout.setColumnStretch(0, 1)
        top_bar_layout.setColumnStretch(1, 1)
        top_bar_layout.setColumnStretch(2, 1)

        back_btn = QPushButton("← 뒤로가기")
        back_btn.clicked.connect(on_back)

        category_label = QLabel(selected_category)
        category_label.setAlignment(Qt.AlignCenter)
        category_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        top_bar_layout.addWidget(back_btn, 0, 0, alignment=Qt.AlignLeft)
        top_bar_layout.addWidget(category_label, 0, 1, alignment=Qt.AlignHCenter)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignTop)

        columns_per_row = 3

        for index, product in enumerate(products):
            row = index // columns_per_row
            col = index % columns_per_row

            item = ProductItem(product, open_product_detail)
            grid_layout.addWidget(item, row, col)

        scroll_widget.setLayout(grid_layout)
        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_bar_layout)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
