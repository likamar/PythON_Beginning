from shop.order import Order, order_info, generate_random_order
from shop.product import Product, product_info, generate_random_product

products = [
    Product(name="apple", category="fruits", unit_price=4.5),
    Product(name="bread", category="breadstuff", unit_price=4.99),
    Product(name="milk", category="diary", unit_price=3.59),
    Product(name="chocolate", category="sweets", unit_price=5.99),
    Product(name="ham", category="meat", unit_price=49.99)
]

if __name__ == "__main__":
    for product in products:
        product_info(product)

    test_product = generate_random_product(5)
    product_info(test_product)

    order_1 = Order(customer_name="Tom", customer_surname="Jones", products_list=products)
    order_info(order_1)
    print("\nRandom order:")
    random_order = generate_random_order(5)
    order_info(random_order)
