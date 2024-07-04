from .product import Product
from typing import Self


class OrderElement:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def order_element_price(self) -> float:
        return self.product.unit_price * self.quantity

    def order_element_info(self):
        self.product.product_info()
        print(f"Quantity: {self.quantity}")
        print(f"Element price: {self.order_element_price():.2f}\n")

    def __str__(self):
        return (f"{self.product}\nQuantity: {self.quantity}\n"
                f"Element price: {self.order_element_price():.2f}\n")

    def __eq__(self, other: Self):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity
