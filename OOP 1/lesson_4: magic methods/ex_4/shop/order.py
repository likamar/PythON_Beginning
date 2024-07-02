import random
from typing import Self

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

    def __str__(self):
        customer_details = f"Customer: {self.customer_name} {self.customer_surname}"
        total_price = f"Total price: {self.total_price:.2f}"
        order_elements = "Order elements:\n"
        for element in self.order_elements:
            order_elements += f"{element}\n"
        return f"{customer_details}\n{total_price}\n\n{order_elements}"

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other: Self):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self.order_elements) != len(other.order_elements):
            return False

        if self.customer_name != other.customer_name or self.customer_surname != other.customer_surname:
            return False

        if self.total_price != other.total_price:
            return False

        # Making a copy of other.order_elements to modify list
        other_order_elements_copy = other.order_elements.copy()
        for order_element in self.order_elements:
            if order_element in other_order_elements_copy:
                # if order_element is on the list - remove it
                other_order_elements_copy.remove(order_element)
            else:
                return False
        # if copy of the list is empty == all elements were similar
        return len(other_order_elements_copy) == 0

        # for order_element in self.order_elements:
        #     if order_element not in other.order_elements:
        #         return False
        #     return True


def generate_random_order():
    order_elements = []
    number_of_elements = random.randint(1, 10)
    for i in range(1, number_of_elements + 1):
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(generate_random_product(i), quantity))
    return Order("test_name", "test_surname", order_elements)
