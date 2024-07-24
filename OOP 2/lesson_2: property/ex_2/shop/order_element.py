from typing import Self

from .product import Product
from .tax_calculator import TaxCalculator



class OrderElement:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def order_element_net_price(self) -> float:
        return self.product.unit_price * self.quantity

    def order_element_gross_price(self):
        return self.order_element_net_price() + TaxCalculator.calculate_tax(self)

    def order_element_info(self):
        self.product.product_info()
        print(f"Quantity: {self.quantity}")
        print(f"Net price: {self.order_element_net_price():.2f}\n")
        print(f"Tax({TaxCalculator.get_tax_rate() * 100}%): {TaxCalculator.calculate_tax(self):.2f}\n")
        print(f"Gross price: {self.order_element_gros_price():.2f}\n")

    def __str__(self):
        return (f"{self.product}\nQuantity: {self.quantity}\n"
                f"Net price: {self.order_element_net_price():.2f}\n"
                f"Tax({TaxCalculator.get_tax_rate(self) * 100:.2f}%): {TaxCalculator.calculate_tax(self):.2f}\n"
                f"Gross price: {self.order_element_gross_price():.2f}\n")

    def __eq__(self, other: Self):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity
