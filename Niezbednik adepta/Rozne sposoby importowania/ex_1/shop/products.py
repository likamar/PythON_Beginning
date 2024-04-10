products = [
    {"name": "bread", "price": 4, "quantity": 20},
    {"name": "milk", "price": 3.5, "quantity": 10},
    {"name": "cheese", "price": 5.99, "quantity": 5}
]


def get_product_by_name(name):
    for product in products:
        if product["name"] == name:
            return product


def is_in_stock(product_name, ordered_quantity):
    product = get_product_by_name(product_name)
    if product is not None and product["quantity"] >= ordered_quantity:
        return True
    return False

