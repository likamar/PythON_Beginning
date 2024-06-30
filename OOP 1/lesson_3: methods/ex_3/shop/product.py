import random


class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def product_info(self):
        print(f"{self.name}, category: {self.category}, unit price: {self.unit_price:.2f}")


def generate_random_product(product_number: int = 1) -> Product:
    product_name = "Product_" + str(product_number)
    category = "test_category"
    price = round(random.uniform(1, 10), 2)
    return Product(product_name, category, price)
