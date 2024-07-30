from shop.product import Product
from shop.order import Order
from shop.discount_policy import default_policy, loyal_customer_policy, christmas_policy
from shop.data_generator import generate_random_order_elements, generate_random_order
from shop.expiring_product import ExpiringProduct
from shop.express_order import ExpressOrder


if __name__ == '__main__':

    order_elements = generate_random_order_elements()
    delivery_date = "2024-08-01"
    customer_name = "Jan"
    customer_surname = "Kowalski"
    discount_policy = loyal_customer_policy
    express_order = ExpressOrder(delivery_date, customer_name, customer_surname, order_elements, discount_policy)

    print(express_order)
