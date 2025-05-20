from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt

from service.ProductService import ProductService
from util.format_price import format_price

class OrderPaymentUI(QWidget):
    def __init__(self, product, discounted_price, count, open_complete_order, on_back):
        super().__init__()
        self.product = product
        self.product_service = ProductService()
        self.open_complete_order = open_complete_order

        back_btn = QPushButton("← 뒤로가기")
        back_btn.clicked.connect(on_back)

        user_info_layout = QFormLayout()
        self.user_name_input = QLineEdit()
        user_info_layout.addRow("이름", self.user_name_input)
        self.user_phone_number_input = QLineEdit()
        user_info_layout.addRow("전화번호", self.user_phone_number_input)
        self.user_address_input = QLineEdit()
        user_info_layout.addRow("배송지", self.user_address_input)


        for input_widget in [self.user_name_input, self.user_phone_number_input, self.user_address_input]:
            input_widget.setMinimumWidth(250)
            input_widget.setFixedHeight(30)


        user_section = QVBoxLayout()
        user_header_label = QLabel("주문자 정보")
        user_header_label.setObjectName("headerLabel")
        user_section.addWidget(user_header_label)
        user_section.addLayout(user_info_layout)

        payment_info_layout = QFormLayout()


        card_list = ["국민", "신한", "우리"]
        self.card_combo_box = QComboBox()
        for card in card_list:
            self.card_combo_box.addItem(card)
        payment_info_layout.addRow("카드 선택", self.card_combo_box)
        self.payment_card_number_input = QLineEdit()
        payment_info_layout.addRow("카드번호", self.payment_card_number_input)

        for input_widget in [self.payment_card_number_input, self.card_combo_box]:
            input_widget.setMinimumWidth(250)
            input_widget.setFixedHeight(30)

        payment_section = QVBoxLayout()
        payment_header_label = QLabel("결제 정보")
        payment_header_label.setObjectName("headerLabel")
        payment_section.addWidget(payment_header_label)
        payment_section.addLayout(payment_info_layout)

        order_info_layout = QVBoxLayout()
        order_info_header_label = QLabel("주문 정보")
        order_info_header_label.setObjectName("headerLabel")
        order_info_layout.addWidget(order_info_header_label)

        image_label = QLabel()
        pixmap = QPixmap(self.product["image_path"]).scaled(100, 100, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        product_text_layout = QVBoxLayout()
        product_text_layout.addWidget(QLabel(f"{self.product['brand']}/{self.product['release_year']}"))
        product_name_label = QLabel(self.product['name'])
        product_name_label.setObjectName("headerLabel")
        product_text_layout.addWidget(product_name_label)
        product_text_layout.addWidget(QLabel(format_price(self.product['price'])))
        product_text_layout.addWidget(QLabel(f"수량 {count}"))

        product_info_layout = QHBoxLayout()
        product_info_layout.addWidget(image_label)
        product_info_layout.addLayout(product_text_layout)

        order_info_layout.addLayout(product_info_layout)

        left_layout = QVBoxLayout()
        left_layout.addWidget(back_btn, alignment=Qt.AlignLeft)
        left_layout.addLayout(user_section)
        left_layout.addLayout(payment_section)
        left_layout.addLayout(order_info_layout)

        summary_layout = QVBoxLayout()
        summary_layout.setAlignment(Qt.AlignTop)
        summary_layout.addStretch()

        summary_layout.addWidget(QLabel(f"할인 전 금액 {format_price(int(product['price']) * count)}"))
        summary_layout.addWidget(QLabel(f"할인율 {round(discounted_price/int(product['price']) * 100)}%"))
        summary_layout.addWidget(QLabel(f"할인 후 금액 {format_price(discounted_price* count)}"))
        summary_layout.addSpacing(20)
        total_price = QLabel(f"최종 금액 {format_price(discounted_price * count)}")
        total_price.setObjectName("headerLabel")
        summary_layout.addWidget(total_price)

        pay_button = QPushButton("결제하기")
        pay_button.clicked.connect(self.on_click_pay)
        summary_layout.addWidget(pay_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(summary_layout, 1)

        self.setLayout(main_layout)

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