from shop.order import generate_random_order

if __name__ == '__main__':
    print("\nRandom order:\n")
    random_order = generate_random_order()
    random_order.order_info()
