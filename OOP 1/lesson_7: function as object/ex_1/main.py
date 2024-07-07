import random

from shop.order import Order

if __name__ == '__main__':

    orders_list = []

    for _ in range(1, 10):
        order_elements_number = random.randint(1, 10)
        orders_list.append(Order.generate_random_order(order_elements_number))

    def get_order_price(order: Order):
        return order.total_price

    def sort_orders(orders_list: list, order_price):
        orders_list.sort(key=order_price)
        return orders_list

    print("Unordered list:")
    for order in orders_list:
        print(f"{order.total_price:.2f}")

    sorted_orders_list = sort_orders(orders_list, get_order_price)

    print("Ordered list:")
    for order in sorted_orders_list:
        print(f"{order.total_price:.2f}")
