from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QListWidgetItem, QInputDialog
)

from service.ProductService import ProductService


class OrderSearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("주문 내역 검색")
        self.setModal(True)
        self.setFixedSize(400, 400)
        self.product_service = ProductService()

        self.selected_product = None
        self.selected_condition = None

        layout = QVBoxLayout()

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("상품명을 입력하세요")
        search_btn = QPushButton("검색")

        search_btn.clicked.connect(self.search_orders)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_btn)
        layout.addLayout(search_layout)

        self.result_list = QListWidget()
        self.result_list.itemDoubleClicked.connect(self.on_item_double_clicked)

        layout.addWidget(self.result_list)
        all_products = self.product_service.find_bought_products_by_name(name="")

        for product in all_products:
            item_text = f"{product['name']} | {product['price']}원 | {product['bought_year']}"
            self.result_list.addItem(QListWidgetItem(item_text))

        close_btn = QPushButton("닫기")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

    def search_orders(self):
        keyword = self.search_input.text()
        self.result_list.clear()

        if not keyword:
            return

        products = self.product_service.find_bought_products_by_name(name=keyword)
        for product in products:
            item_text = f"{product['name']} | {product['price']}원 | {product['bought_year']}"
            self.result_list.addItem(QListWidgetItem(item_text))

        if self.result_list.count() == 0:
            self.result_list.addItem(QListWidgetItem("검색 결과가 없습니다."))

    def on_item_double_clicked(self, item):
        name = item.text().split("|")[0].strip()
        product = self.product_service.find_exact_bought_product_by_name(name)

        if product:
            condition, ok = QInputDialog.getItem(
                self,
                "상품 상태 선택",
                "이 상품의 상태를 선택하세요:",
                ["상", "중", "하"],
                0,
                False
            )

            if ok:
                self.selected_product = product
                self.selected_condition = condition
                self.accept()
