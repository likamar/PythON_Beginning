from shop.product import Product
from shop.order import generate_random_order

if __name__ == '__main__':
    new_order = generate_random_order(20)
    print(new_order)
    new_product = Product(name='New Product', category="new_category", unit_price=5.99)
    new_product_quantity = 10
    new_order.add_product_to_order(new_product, new_product_quantity)
    print(new_order)
