import random

from shop.order import Order

if __name__ == '__main__':

    orders_list = []

    for _ in range(1, 10):
        order_elements_number = random.randint(1, 10)
        orders_list.append(Order.generate_random_order(order_elements_number))

    def get_order_price(order: Order):
        return order.total_price

    print("Unordered list:")
    for order in orders_list:
        print(f"{order.total_price:.2f}")

    print("Ordered list:")
    orders_list.sort(key=lambda order: order.total_price)
    for order in orders_list:
        print(f"{order.total_price:.2f}")
