from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order

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

    order_element_1 = OrderElement(product=product_1, quantity=1)
    order_element_2 = OrderElement(product=product_2, quantity=1)
    order_element_3 = OrderElement(product=product_3, quantity=1)
    order_element_4 = OrderElement(product=product_1, quantity=4)

    print(order_element_1 == order_element_2)
    print(order_element_1 == order_element_3)
    print(order_element_1 == order_element_4)
    print(order_element_2 == order_element_3)
    print(order_element_2 == order_element_4)
    print(order_element_3 == order_element_4)

    # return NotImplemented
    print(product_1 == order_element_1)

    order_elements_1 = [order_element_1, order_element_2, order_element_3]
    order_elements_2 = [order_element_1, order_element_2, order_element_3]
    order_elements_3 = [order_element_1, order_element_2, order_element_4]

    order_1 = Order(customer_name="Marcin", customer_surname="Janiak", order_elements=order_elements_1)
    order_2 = Order(customer_name="Marcin", customer_surname="Janiak", order_elements=order_elements_2)
    order_3 = Order(customer_name="Marcin", customer_surname="Kowalski", order_elements=order_elements_1)
    order_4 = Order(customer_name="Marcin", customer_surname="Janiak", order_elements=order_elements_3)

    print("Order elements:")
    print(order_1 == order_2)
    print(order_1 == order_3)
    print(order_1 == order_4)
    print(order_2 == order_3)
    print(order_2 == order_4)
    print(order_3 == order_4)
