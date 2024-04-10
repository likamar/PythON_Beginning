from shop.products import get_product_by_name, is_in_stock

orders_list = []


def get_total_price(price, quantity):
    return float(price * quantity)


def create_order(product_name, quantity):
    if is_in_stock(product_name, quantity):
        product = get_product_by_name(product_name)
        price = product["price"]
        total_price = get_total_price(price, quantity)
        new_order = {
            "name": product_name,
            "quantity": quantity,
            "total_price": total_price
        }
        add_to_orders_list(new_order)
        return new_order
    else:
        return None


def add_to_orders_list(new_order):
    orders_list.append(new_order)

