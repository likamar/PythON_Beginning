from shop.order import create_order
from shop.order import orders_list


def init_shop():
    print("Welcome to the shop!")
    product_name = input("Product name: ")
    quantity = int(input("Quantity: "))
    user_order = create_order(product_name, quantity)

    if user_order is not None:
        total_price = user_order["total_price"]
        print (user_order)
        print (orders_list)
        print(f"To pay: {total_price:.2f} EUR")
    else:
        print("Out of stock")


if __name__ == "__main__":
    init_shop()
