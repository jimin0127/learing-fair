from service.MyProductReository import MyProductRepository
from service.ProductRepository import ProductRepository


class ProductService:
    def __init__(self):
        self.productRepository = ProductRepository()
        self.myProductRepository = MyProductRepository()

    def find_all(self):
        return self.productRepository.find_all()

    def find_all_by_category(self, category):
        return self.productRepository.find_all_by_category(category)

    def save_bought_product(self, product):
        self.myProductRepository.save(product)

    def find_all_bought_product(self):
        return self.myProductRepository.find_all()

    def find_bought_products_by_name(self, name):
        return self.myProductRepository.find_all_by_name(name)

    def find_exact_bought_product_by_name(self, name):
        return self.myProductRepository.find_by_name(name)
