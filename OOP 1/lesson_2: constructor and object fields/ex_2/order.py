from product import products


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


order_1 = Order(customer_name="Tom", customer_surname="Jones", products_list=products)

print("Order_1:")
print(f"Customer Name: {order_1.customer_name}")
print(f"Customer Surname: {order_1.customer_surname}")
print(f"products_list:")
for product in order_1.products_list:
    print(f"Product: {product.name}, category: {product.category}, unit price: {product.unit_price}")
print(f"total_price: {order_1.total_price}")
