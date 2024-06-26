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

for product in products:
    print(f"Product: {product.name}, category: {product.category}, unit price: {product.unit_price}")
