from product import products, product_info, Product,


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
    print(f"Customer Name: {order.customer_name}\nCustomer Surname: {order.customer_surname}")
    print("Products: ")
    for product in order.products_list:
        product_info(product)


def generate_random_order(number_of_products: int=1):
    products_list = []
    for i in range(1, number_of_products + 1):
        products_list.append(Product(name="Product_" + str(i), category="test", unit_price=1))


if __name__ == "__main__":
    order_1 = Order(customer_name="Tom", customer_surname="Jones", products_list=products)
    order_info(order_1)
    generate_random_order(5)