import random
from typing import Self

from .order_element import OrderElement
from .product import Product
from .discount_policy import default_policy, christmas_policy, loyal_customer_policy


class Order:
    MAX_ORDER_ELEMENTS = 2

    def __init__(self, customer_name, customer_surname, order_elements: list = None, discount_policy=None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            self._order_elements = order_elements[0:Order.MAX_ORDER_ELEMENTS]
        else:
            self._order_elements = order_elements
        if discount_policy is None:
            self.discount_policy = default_policy
        else:
            self.discount_policy = discount_policy
        self.total_price = self._calc_total_price()

    def calc_price_before_discount(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.order_element_gross_price()
        return total_price

    def _calc_total_price(self):
        return self.discount_policy(self.calc_price_before_discount())

    def get_discount_value(self):
        return self.total_price - self.calc_price_before_discount()

    def order_info(self):
        print(f"Customer: {self.customer_name} {self.customer_surname}")
        print(f"Total price: {self.total_price:.2f}")
        print("Order elements:\n ")
        for element in self._order_elements:
            element.order_element_info()

    def __str__(self):
        customer_details = f"\nCustomer: {self.customer_name} {self.customer_surname}"
        total_price = f"Total price: {self.total_price:.2f}"
        discount_value = f"Discount: {self.get_discount_value():.2f}"
        order_elements = f"Order elements({len(self)}):\n\n"
        mark_line = "-" * 50
        for element in self._order_elements:
            order_elements += f"{element}\n"
        return f"{customer_details}\n{total_price}\n{discount_value}\n{order_elements}{mark_line}"

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other: Self):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_elements) != len(other._order_elements):
            return False

        if self.customer_name != other.customer_name or self.customer_surname != other.customer_surname:
            return False

        if self.total_price != other.total_price:
            return False

        # Making a copy of other.order_elements to modify list
        other_order_elements_copy = other._order_elements.copy()
        for order_element in self._order_elements:
            if order_element in other_order_elements_copy:
                # if order_element is on the list - remove it
                other_order_elements_copy.remove(order_element)
            else:
                return False
        # if copy of the list is empty == all elements were similar
        return len(other_order_elements_copy) == 0

    def add_product_to_order(self, product: Product, quantity: int):
        if len(self) >= Order.MAX_ORDER_ELEMENTS:
            print(f"Reached maximum number of elements! ({Order.MAX_ORDER_ELEMENTS})")
        else:
            new_order_element = OrderElement(product, quantity)
            self._order_elements.append(new_order_element)
            self.total_price = self._calc_total_price()
