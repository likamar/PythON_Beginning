class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


def product_info(product: Product):
    print(f"{product.name}, category: {product.category}, unit price: {product.unit_price}")


def generate_random_product(product_number: int) -> Product:
    product_name = "Product_" + str(product_number)
    category = "test_category"
    price = 1
    return Product(product_name, category, price)
