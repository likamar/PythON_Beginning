class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


products = [
    Product(name="apple", category="fruits", unit_price=4.5),
    Product(name="bread", category="breadstuff", unit_price=4.99),
    Product(name="milk", category="diary", unit_price=3.59),
    Product(name="chocolate", category="sweets", unit_price=5.99),
    Product(name="ham", category="meat", unit_price=49.99)
]


def product_info(product: Product):
    print(f"{product.name}, category: {product.category}, unit price: {product.unit_price}")


def generate_random_product(product_number: int) -> Product:
    product_name = "Product_" + str(product_number)
    category = "test_category"
    price = 1
    return Product(product_name, category, price)


if __name__ == "__main__":
    for product in products:
        product_info(product)

    test_product = generate_random_product(5)
    product_info(test_product)
