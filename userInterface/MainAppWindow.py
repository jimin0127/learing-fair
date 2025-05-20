from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from apply_global_theme import apply_global_theme
from userInterface.OrderCompleteUI import OrderCompleteUI
from userInterface.OrderPaymentUI import OrderPaymentUI
from userInterface.ProductDetailUI import ProductDetailUI
from userInterface.SelectCategoryUI import SelectCategoryUI
from userInterface.SelectProductUI import SelectProductUI
from userInterface.StartScreen import StartScreen


class MainAppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("헌옷줄게 새옷다오")
        self.resize(800, 600)

        self.stack = QStackedWidget()
        self.view_history = []

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.start_screen = StartScreen(on_start_clicked=self.open_select_category_ui)
        self.push_view(self.start_screen)


    def open_select_category_ui(self):
        select_category_ui = SelectCategoryUI(self.on_select_category)
        self.push_view(select_category_ui)

    def open_select_product_ui(self, selected_category):
        select_product_ui = SelectProductUI(
            open_product_detail=lambda product: self.open_product_detail(product),
            selected_category=selected_category,
            on_back=self.pop_view,
        )
        self.push_view(select_product_ui)

    def open_product_detail(self, product):
        detail_view = ProductDetailUI(
            product=product,
            open_order_payment=lambda p, dp, c: self.open_order_payment(p, dp, c),
            on_back=self.pop_view,
        )

        self.push_view(detail_view)

    def open_order_payment(self, product, discounted_price, count):
        order_payment_view = OrderPaymentUI(
            product=product,
            discounted_price=discounted_price,
            count=count,
            open_complete_order=self.open_complete_order,
            on_back=self.pop_view,
        )
        self.push_view(order_payment_view)

    def open_complete_order(self):
        order_complete_view = OrderCompleteUI(on_go_home=self.on_go_home)
        self.push_view(order_complete_view)

    def on_go_home(self):
        self.view_history.clear()
        self.start_screen = StartScreen(on_start_clicked=self.open_select_category_ui)
        self.push_view(self.start_screen)

    def on_select_category(self, selected_category):
        self.open_select_product_ui(selected_category)

    def push_view(self, widget: QWidget):
        self.view_history.append(widget)
        self.stack.addWidget(widget)
        self.stack.setCurrentWidget(widget)

    def pop_view(self):
        if len(self.view_history) <= 1:
            return
        current = self.view_history.pop()
        self.stack.removeWidget(current)
        self.stack.setCurrentWidget(self.view_history[-1])
