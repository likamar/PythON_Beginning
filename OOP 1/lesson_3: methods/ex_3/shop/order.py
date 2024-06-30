import random

from .product import generate_random_product
from .order_element import OrderElement


class Order:
    def __init__(self, customer_name, customer_surname, order_elements: list = None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calc_total_price()

    def calc_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.order_element_price()
        return total_price

    def order_info(self):
        print(f"Customer: {self.customer_name} {self.customer_surname}")
        print(f"Total price: {self.total_price:.2f}")
        print("Order elements:\n ")
        for element in self.order_elements:
            element.order_element_info()


def generate_random_order():
    order_elements = []
    number_of_elements = random.randint(1, 10)
    for i in range(1, number_of_elements + 1):
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(generate_random_product(i), quantity))
    return Order("test_name", "test_surname", order_elements)
