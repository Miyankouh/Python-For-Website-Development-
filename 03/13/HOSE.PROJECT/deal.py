from base import BaseClass


class Sell(BaseClass):
    def __init__(self, price_per_meter, discountable, convertable, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price: {self.price_per_meter}\t discont: {self.discountable}\t convert: {self.convertable}")


class Rent(BaseClass):
    def __init__(self, initial_price, montly_price, convertable, discountable, *args, **kwargs):
        self.initial_price = initial_price
        self.montly_price = montly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)