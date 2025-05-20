import csv
import os
from datetime import datetime

MY_PRODUCT_CSV_PATH = 'BoughtProductData.csv'

class MyProductRepository:
    def __init__(self):
        self.csv_path = MY_PRODUCT_CSV_PATH
        self.products = self._load_products()

    def _load_products(self) -> list[dict]:
        with open(self.csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def find_all(self):
        return self.products

    def save(self, product):
        file_exists = os.path.isfile(MY_PRODUCT_CSV_PATH)

        with open(MY_PRODUCT_CSV_PATH, mode="a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "product_id", "category", "name", "brand", "image_path", "price", "bought_year"
            ])

            if not file_exists or os.path.getsize(MY_PRODUCT_CSV_PATH) == 0:
                writer.writeheader()

            writer.writerow({
                "product_id": product["id"],
                "category": product["category"],
                "name": product["name"],
                "brand": product["brand"],
                "image_path": product["image_path"],
                "price": product["price"],
                "bought_year": datetime.now().year,
            })

    def find_all_by_name(self, name):
        return [p for p in self.products if name.lower() in p["name"].lower()]

    def find_by_name(self, name):
        for product in self.products:
            if product["name"] == name:
                return product