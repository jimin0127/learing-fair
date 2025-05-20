import csv

PRODUCT_CSV_PATH = 'ProductData.csv'

class ProductRepository:
    def __init__(self):
        self.csv_path = PRODUCT_CSV_PATH
        self.products = self._load_products()

    def _load_products(self) -> list[dict]:
        with open(self.csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def find_product_by_id(self, target_id: str):
        for product in self.products:
            if product['id'] == str(target_id):
                return product
        return None

    def find_all(self):
        return self.products

    def find_all_by_category(self, category):
        return [p for p in self.products if p["category"] == category]