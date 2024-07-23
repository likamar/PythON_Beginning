from shop.product import Product
from shop.order import Order
from shop.discount_policy import default_policy, loyal_customer_policy, christmas_policy
from shop.data_generator import generate_random_order_elements, generate_random_order

if __name__ == '__main__':
    order_1 = generate_random_order(9)
    print(order_1)
    product_1 = Product(name='New Product', category="new_category", unit_price=5.99)
    new_product_quantity = 10
    order_1.add_product_to_order(product_1, new_product_quantity)
    print(order_1)
    order_1.add_product_to_order(product_1, new_product_quantity)
    print(order_1)

    product_2 = Product(name='Apple', category="fruits and veg", unit_price=4.99)
    order_2_elements = generate_random_order_elements()
    order_2 = Order(customer_name="Jan", customer_surname="Kowalski", order_elements=order_2_elements, discount_policy=loyal_customer_policy)
    print(order_2)

    product_3 = Product(name='beef', category="food", unit_price=164.99)
    order_3_elements = generate_random_order_elements()
    order_3 = Order(customer_name="Adam", customer_surname="Nowak", order_elements=order_3_elements, discount_policy=christmas_policy)
    print(order_3)
