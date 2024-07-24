import random

from .product import Product
from .order_element import OrderElement
from .order import Order

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 99.99

MIN_QUANTITY = 1
MAX_QUANTITY = 10


def generate_random_product(product_number: int = 1) -> Product:
    product_name = "Product_" + str(product_number)
    category = "test_category"
    price = round(random.uniform(MIN_UNIT_PRICE, MAX_UNIT_PRICE), 2)
    return Product(product_name, category, price)


def generate_random_order_elements(number_of_products=None):
    order_elements = []
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS)
    if number_of_products > Order.MAX_ORDER_ELEMENTS:
        number_of_products = Order.MAX_ORDER_ELEMENTS
    for _ in range(number_of_products):
        product = generate_random_product(random.randint(1, 10))
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))
    return order_elements


def generate_random_order(number_of_elements: int):
    order_elements = []
    if number_of_elements > Order.MAX_ORDER_ELEMENTS:
        number_of_elements = Order.MAX_ORDER_ELEMENTS
    for i in range(1, number_of_elements + 1):
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(generate_random_product(i), quantity))
    return Order("test_name", "test_surname", order_elements)
