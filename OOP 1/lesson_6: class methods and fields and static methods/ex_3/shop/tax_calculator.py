class TaxCalculator:
    TAX_RATES = {
        'fruits and veg': 0.05,
        'food': 0.08,
    }
    BASE_TAX_RATE = 0.2

    @staticmethod
    def calculate_tax(order_element):
        tax_rate = TaxCalculator.get_tax_rate(order_element)
        return order_element.order_element_net_price() * tax_rate

    @staticmethod
    def get_tax_rate(order_element):
        product_category = order_element.product.category
        if product_category in TaxCalculator.TAX_RATES:
            return TaxCalculator.TAX_RATES[product_category]
        else:
            return TaxCalculator.BASE_TAX_RATE
