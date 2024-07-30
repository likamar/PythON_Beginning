from .order import Order


class ExpressOrder(Order):

    EXPRESS_DELIVERY_FEE = 20

    def __init__(self, delivery_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        return self.discount_policy(self.calc_price_before_discount()) + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        customer_details = f"\nCustomer: {self.customer_name} {self.customer_surname}"
        total_price = f"Total price: {self.total_price:.2f}"
        discount_value = f"Discount: {self.get_discount_value():.2f}"
        delivery_date = f"Delivery date: {self.delivery_date}"
        extra_fee = f"Express Delivery Fee: {ExpressOrder.EXPRESS_DELIVERY_FEE:.2f}"
        order_elements = f"Order elements({len(self)}):\n\n"
        mark_line = "-" * 50
        for element in self._order_elements:
            order_elements += f"{element}\n"
        order_info = "\n".join([customer_details, total_price, discount_value, delivery_date, extra_fee, order_elements, mark_line])
        return order_info
