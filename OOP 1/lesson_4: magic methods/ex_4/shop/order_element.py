from shop.product import Product


class OrderElement:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity

    def order_element_price(self) -> float:
        return self.product.unit_price * self.quantity

    def order_element_info(self):
        self.product.product_info()
        print(f"Quantity: {self.quantity}")
        print(f"Element price: {self.order_element_price():.2f}\n")

    def __str__(self):
        return (f"{self.product}\nQuantity: {self.quantity}\n"
                f"Element price: {self.order_element_price():.2f}\n")

