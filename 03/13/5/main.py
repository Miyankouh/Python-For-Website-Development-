from test import D, B, E

class Apartment:
    def __init__(self, floor, elevator, *args, **kwargs):
        self.floor = floor
        self.elevator = elevator
        super().__init__(*args, **kwargs)


class House:
    def __init__(self, age, address):
        self.age = age
        self.address = address


class Rent:
    def __init__(self, fixed_amount, monthly_amount):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount


class Sale:
    def __init__(self, fee):
        self.fee = fee


class ApartmentRent(Apartment, Rent):
    def __str__(self):
        return f"{self.floor} {self.fixed_amount}"


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"{self.floor} {self.fee}"


class HouseRate(House, Rent):
    pass


class HouseSale(House, Sale):
    pass


if __name__ == "__main__":
    # e = E()
    # print(E.mro())
    # e.greeting()

    apartment_rent = ApartmentRent(floor=2, elevator=True, fixed_amount=120000000, monthly_amount=1000000)
    apartment_sale = ApartmentSale(floor=2, elevator=True, fee=120000000)
    print(apartment_rent)
    print(apartment_sale)


