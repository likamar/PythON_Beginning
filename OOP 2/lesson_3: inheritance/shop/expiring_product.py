import datetime

from .product import Product


class ExpiringProduct(Product):

    CURRENT_YEAR = datetime.date.today().year

    def __init__(self, name, category, unit_price, manufacture_year, expiration_years):
        super().__init__(name, category, unit_price)
        self.manufacture_year = manufacture_year
        self.expiration_years = expiration_years

    def does_expire(self):
        return ExpiringProduct.CURRENT_YEAR - self.manufacture_year > self.expiration_years
