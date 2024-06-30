from shop.order import Order, generate_random_order

if __name__ == '__main__':
    print("\nRandom order:")
    random_order = generate_random_order()
    random_order.order_info()
