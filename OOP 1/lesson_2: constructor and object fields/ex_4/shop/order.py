from .product import product_info, generate_random_product
import random

class Order:
    def __init__(self, customer_name, customer_surname, products_list=None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if products_list is None:
            products_list = []
        self.products_list = products_list
        self.total_price = self.calc_total_price()

    def calc_total_price(self):
        total_price = 0
        for product in self.products_list:
            total_price += product.unit_price
        return total_price


def order_info(order: Order):
    print(f"Customer: {order.customer_name} {order.customer_surname}")
    print(f"Total price: {order.total_price}")
    print("Products: ")
    for product in order.products_list:
        print("\t", end="")
        product_info(product)


def generate_random_order():
    products_list = []
    number_of_products = random.randint(1, 10)
    for i in range(1, number_of_products + 1):
        products_list.append(generate_random_product(i))
    return Order("test_name", "test_surname", products_list)
