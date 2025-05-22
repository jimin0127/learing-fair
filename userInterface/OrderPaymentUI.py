from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt

from service.ProductService import ProductService
from util.format_price import format_price
from util.get_resource_path import get_resource_path

CARD_LIST = ["국민", "신한", "우리"]

class OrderPaymentUI(QWidget):
    def __init__(self, product, discounted_price, count, open_complete_order, on_back):
        super().__init__()

        self.product = product
        self.product_service = ProductService()
        self.open_complete_order = open_complete_order
        self.on_back = on_back
        self.count = count
        self.discounted_price = discounted_price
        self.payment_card_number_input = None
        self.card_combo_box = None
        self.user_address_input = None
        self.user_phone_number_input = None
        self.user_name_input = None

        self.init_ui()
        
    def init_ui(self):
        back_btn = QPushButton("← 뒤로가기")
        back_btn.clicked.connect(self.on_back)

        user_info_section = self.user_info_section()
        payment_info_section = self.payment_info_section()
        order_info_section = self.order_info_section()

        left_layout = QVBoxLayout()
        left_layout.addWidget(back_btn, alignment=Qt.AlignLeft)
        left_layout.addLayout(user_info_section)
        left_layout.addLayout(payment_info_section)
        left_layout.addLayout(order_info_section)

        right_layout = self.price_summary_section()

        pay_button = QPushButton("결제하기")
        pay_button.clicked.connect(self.on_click_pay)
        right_layout.addWidget(pay_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 1)

        self.setLayout(main_layout)

    def user_info_section(self):
        user_header_label = QLabel("주문자 정보")
        user_header_label.setObjectName("headerLabel")

        self.user_name_input = QLineEdit()
        self.user_phone_number_input = QLineEdit()
        self.user_address_input = QLineEdit()
        user_info_layout = QFormLayout()
        user_info_layout.addRow("이름", self.user_name_input)
        user_info_layout.addRow("전화번호", self.user_phone_number_input)
        user_info_layout.addRow("배송지", self.user_address_input)

        for input_widget in [self.user_name_input, self.user_phone_number_input, self.user_address_input]:
            input_widget.setMinimumWidth(250)
            input_widget.setFixedHeight(30)

        user_section = QVBoxLayout()

        user_section.addWidget(user_header_label)
        user_section.addLayout(user_info_layout)

        return user_section

    def payment_info_section(self):
        payment_header_label = QLabel("결제 정보")
        payment_header_label.setObjectName("headerLabel")

        self.card_combo_box = QComboBox()
        for card in CARD_LIST:
            self.card_combo_box.addItem(card)
        self.payment_card_number_input = QLineEdit()

        payment_info_layout = QFormLayout()
        payment_info_layout.addRow("카드 선택", self.card_combo_box)
        payment_info_layout.addRow("카드번호", self.payment_card_number_input)

        for input_widget in [self.payment_card_number_input, self.card_combo_box]:
            input_widget.setMinimumWidth(250)
            input_widget.setFixedHeight(30)

        payment_section = QVBoxLayout()
        payment_section.addWidget(payment_header_label)
        payment_section.addLayout(payment_info_layout)

        return payment_section

    def order_info_section(self):
        order_info_layout = QVBoxLayout()
        order_info_header_label = QLabel("주문 정보")
        order_info_header_label.setObjectName("headerLabel")
        order_info_layout.addWidget(order_info_header_label)

        image_label = QLabel()
        pixmap = QPixmap(get_resource_path(self.product["image_path"])).scaled(100, 100, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        product_text_layout = QVBoxLayout()
        product_text_layout.addWidget(QLabel(f"{self.product['brand']}/{self.product['release_year']}"))
        product_name_label = QLabel(self.product['name'])
        product_name_label.setObjectName("headerLabel")
        product_text_layout.addWidget(product_name_label)
        product_text_layout.addWidget(QLabel(format_price(self.product['price'])))
        product_text_layout.addWidget(QLabel(f"수량 {self.count}"))

        product_info_layout = QHBoxLayout()
        product_info_layout.addWidget(image_label)
        product_info_layout.addLayout(product_text_layout)

        order_info_layout.addLayout(product_info_layout)

        return order_info_layout

    def price_summary_section(self):
        before_total_price = format_price(self.get_total_price())
        discount_rate = self.calculate_discount_rate()
        discounted_total_price = format_price(self.get_discounted_price())

        before_total_price_label = QLabel(f"할인 전 금액 {before_total_price}")
        discount_rate = QLabel(f"할인율 {discount_rate}%")
        discounted_total_price_label = QLabel(f"할인 후 금액 {discounted_total_price}")
        total_price_label = QLabel(f"최종 금액 {format_price(self.discounted_price * self.count)}")
        total_price_label.setObjectName("headerLabel")

        summary_layout = QVBoxLayout()
        summary_layout.setAlignment(Qt.AlignTop)
        summary_layout.addStretch()

        summary_layout.addWidget(before_total_price_label)
        summary_layout.addWidget(discount_rate)
        summary_layout.addWidget(discounted_total_price_label)
        summary_layout.addSpacing(20)
        summary_layout.addWidget(total_price_label)

        return summary_layout

    def get_total_price(self):
        return int(self.product['price']) * self.count

    def get_discounted_price(self):
        return self.discounted_price * self.count

    def on_click_pay(self):
        if not self.user_name_input.text().strip():
            self.show_warning("이름을 입력해주세요.")
            return
        if not self.user_phone_number_input.text().strip():
            self.show_warning("전화번호를 입력해주세요.")
            return
        if not self.user_address_input.text().strip():
            self.show_warning("배송지를 입력해주세요.")
            return
        if not self.payment_card_number_input.text().strip():
            self.show_warning("카드번호를 입력해주세요.")
            return
        if self.card_combo_box.currentIndex() < 0:
            self.show_warning("카드를 선택해주세요.")
            return

        self.open_complete_order()
        self.product_service.save_bought_product(self.product)

    def show_warning(self, message: str):
        QMessageBox.warning(self, "입력 오류", message)

    def calculate_discount_rate(self):
        before_price = int(self.product['price'])
        discount_amount = before_price - self.discounted_price
        discount_rate = (discount_amount / before_price) * 100

        return round(discount_rate, 1)
