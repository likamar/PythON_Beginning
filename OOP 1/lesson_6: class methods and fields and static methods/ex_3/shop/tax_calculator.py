class TaxCalculator:
    TAX_RATES = {
        'fruits and veg': 0.05,
        'food': 0.08,
        'other': 0.20
    }

    @staticmethod
    def calculate_tax(order_element):
        tax_rate = TaxCalculator.get_tax_rate(order_element)
        return order_element.order_element_net_price() * tax_rate

    @staticmethod
    def get_tax_rate(order_element):
        if order_element.product.category == 'fruits and veg':
            tax_rate = TaxCalculator.TAX_RATES['fruits and veg']
        elif order_element.product.category == 'food':
            tax_rate = TaxCalculator.TAX_RATES['food']
        else:
            tax_rate = TaxCalculator.TAX_RATES['other']
        return tax_rate
