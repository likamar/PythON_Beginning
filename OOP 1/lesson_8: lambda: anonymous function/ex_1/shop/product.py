import random

from typing import Self


class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def product_info(self):
        print(f"{self.name}, category: {self.category}, unit price: {self.unit_price:.2f}")

    def __str__(self):
        return f"{self.name}, category: {self.category}, unit price: {self.unit_price:.2f}"

    def __eq__(self, other: Self):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and self.category == other.category and self.unit_price == other.unit_price


def generate_random_product(product_number: int = 1) -> Product:
    product_name = "Product_" + str(product_number)
    category = "test_category"
    price = round(random.uniform(1, 10), 2)
    return Product(product_name, category, price)
