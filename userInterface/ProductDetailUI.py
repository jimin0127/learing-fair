from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QDialog, QSpinBox
from PySide6.QtCore import Qt

from service.PriceCalculator import calculator_price
from service.ProductService import ProductService
from userInterface.OrderSearchDialog import OrderSearchDialog
from util.format_price import format_price
from util.get_resource_path import get_resource_path


class ProductDetailUI(QWidget):
    def __init__(self, product, open_order_payment, on_back):
        super().__init__()

        self.total_price_label = None
        self.count_box = None
        self.after_price_label = None
        self.price_label = None
        self.bought_pixmap = None
        self.bought_pixmap_label = None
        self.bought_year = None
        self.condition_label = None
        self.bought_product_label = None
        self.bought_product_header_label = None
        self.info_layout =  QVBoxLayout()
        self.product = product
        self.product_service = ProductService()
        self.open_order_payment = open_order_payment
        self.bought_products = self.product_service.find_all_bought_product()
        self.on_back = on_back

        self.selected_product = None
        self.selected_condition = None

        self.unit_ui()

    def unit_ui(self):
        back_btn = QPushButton("← 뒤로가기")
        back_btn.clicked.connect(self.on_back)

        top_bar_layout = QHBoxLayout()
        top_bar_layout.addWidget(back_btn)
        top_bar_layout.addStretch()

        pixmap = QPixmap(get_resource_path(self.product["image_path"])).scaled(300, 300, Qt.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        bought_info_layout = self.get_bought_info_layout()

        purchase_btn = QPushButton("구매하기")
        purchase_btn.setStyleSheet("font-weight: bold; padding: 8px;")
        purchase_btn.clicked.connect(self.on_purchase)


        self.init_product_info_section()
        self.info_layout.addSpacing(10)
        self.init_select_bought_product_button()
        self.info_layout.addLayout(bought_info_layout)
        self.info_layout.addSpacing(10)
        self.init_price_discount_info_section()
        self.info_layout.addSpacing(10)
        self.info_layout.addWidget(purchase_btn)

        content_layout = QHBoxLayout()
        content_layout.addWidget(image_label)
        content_layout.addSpacing(40)
        content_layout.addLayout(self.info_layout)

        layout = QVBoxLayout()
        layout.addLayout(top_bar_layout)
        layout.addLayout(content_layout)
        self.setLayout(layout)

        self.resize(300, 400)

    def init_product_info_section(self):
        brand_label = QLabel(self.product['brand'])
        brand_label.setObjectName("brandLabel")

        name_label = QLabel(self.product['name'])
        name_label.setObjectName("nameLabel")

        before_price_label = QLabel(format_price(self.product['price']))

        self.info_layout.addWidget(brand_label)
        self.info_layout.addWidget(name_label)
        self.info_layout.addWidget(before_price_label)

    def init_select_bought_product_button(self):
        select_bought_product_button = QPushButton("구매했던 옷 반환하고 할인 받기")
        select_bought_product_button.clicked.connect(self.on_select_bought_product)

        self.info_layout.addWidget(select_bought_product_button)

    def get_bought_info_layout(self):
        self.bought_product_header_label = QLabel()
        self.bought_product_header_label.setObjectName("headerLabel")

        self.info_layout.addWidget(self.bought_product_header_label)

        self.bought_product_label = QLabel()
        self.condition_label = QLabel()
        self.bought_year = QLabel()
        self.bought_pixmap_label = QLabel()
        self.bought_pixmap = QPixmap()
        self.bought_pixmap_label.setPixmap(self.bought_pixmap)

        bought_info_layout = QHBoxLayout()

        bought_text_layout = QVBoxLayout()

        bought_text_layout.addWidget(self.bought_product_label)
        bought_text_layout.addWidget(self.condition_label)
        bought_text_layout.addWidget(self.bought_year)

        self.bought_pixmap_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        bought_info_layout.addWidget(self.bought_pixmap_label)
        bought_info_layout.addLayout(bought_text_layout)

        return bought_info_layout

    def init_price_discount_info_section(self):
        self.price_label = QLabel("가격 할인 정보")
        self.price_label.setObjectName("headerLabel")
        self.after_price_label = QLabel(f"할인된 가격: {format_price(self.product['price'])}")

        self.count_box = QSpinBox()
        self.count_box.setRange(1, 10)
        self.count_box.setValue(1)
        self.count_box.valueChanged.connect(self.update_total_price)

        quantity_layout = QHBoxLayout()
        quantity_label = QLabel("수량")
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addStretch()
        quantity_layout.addWidget(self.count_box)

        self.total_price_label = QLabel(f"총 가격 (1개): {format_price(self.product['price'])}")
        self.total_price_label.setObjectName("headerLabel")
        self.total_price_label.setStyleSheet("margin: 6px 0px;")

        self.info_layout.addWidget(self.price_label)
        self.info_layout.addWidget(self.after_price_label)
        self.info_layout.addLayout(quantity_layout)
        self.info_layout.addWidget(self.total_price_label)


    def on_purchase(self):
        count = self.count_box.value()

        if self.selected_product == None:
            calculated_price = int(self.product['price'])
        else:
            calculated_price = calculator_price(
                price=self.product['price'],
                quality=self.selected_condition,
                buy_count=1,
                bought_product=self.selected_product,
            )

        self.open_order_payment(
            self.product,
            calculated_price,
            count
        )

    def on_select_bought_product(self):
        dialog = OrderSearchDialog()
        result = dialog.exec()

        if result == QDialog.Accepted and dialog.selected_product and dialog.selected_condition:
            self.selected_product = dialog.selected_product
            self.selected_condition = dialog.selected_condition
            self.update_view(dialog.selected_product, dialog.selected_condition)

    def update_view(self, bought_product, selected_condition):
        self.bought_product_header_label.setText("반환할 상품")
        self.bought_pixmap = QPixmap(get_resource_path(bought_product["image_path"])).scaled(100, 100, Qt.KeepAspectRatio)
        self.bought_pixmap_label.setPixmap(self.bought_pixmap)
        self.bought_product_label.setText(bought_product['name'])
        self.condition_label.setText(f"<b>상태</b> {selected_condition}")
        self.bought_year.setText(f"<b>구매연도</b> {bought_product['bought_year']}")
        self.count_box.setValue(1)
        self.update_total_price()

        if bought_product is None:
            calculated_price = int(self.product['price'])
        else:
            calculated_price = calculator_price(
                price=self.product['price'],
                quality=selected_condition,
                buy_count=1,
                bought_product=bought_product,
            )

        self.after_price_label.setText(f"할인된 가격: {format_price(calculated_price)}")

    def update_total_price(self):
        if not hasattr(self, 'selected_condition') or not hasattr(self, 'selected_condition'):
            return

        count = self.count_box.value()

        if self.selected_product is None:
            calculated_price = int(self.product['price']) * count
        else:
            calculated_price = calculator_price(
                price=self.product['price'],
                quality=self.selected_condition,
                buy_count=count,
                bought_product=self.selected_product,
            )

        self.total_price_label.setText(f"총 가격 ({count}개): {format_price(calculated_price)}")
