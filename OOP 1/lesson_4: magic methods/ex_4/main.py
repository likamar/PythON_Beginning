from shop.product import Product
from shop.order import generate_random_order

if __name__ == '__main__':
    product_1 = Product(name="coca-cola", category="beverages", unit_price=5.99)
    product_2 = Product(name="coca-cola", category="beverages", unit_price=5.99)
    product_3 = Product(name="Coca-cola", category="beverages", unit_price=5.99)
    product_4 = Product(name="coca-cola", category="beverages", unit_price=6.99)
    print(product_1 == product_2)
    print(product_1 == product_3)
    print(product_1 == product_4)
    print(product_2 == product_3)
    print(product_2 == product_4)
    print(product_3 == product_4)
