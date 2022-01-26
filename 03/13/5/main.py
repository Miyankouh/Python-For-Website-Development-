from abc import ABC, abstractmethod

class Apartment:
    def __init__(self, floor, elevator, *args, **kwargs):
        self.floor = floor
        self.elevator = elevator
        super().__init__(*args, **kwargs)


class House:
    def __init__(self, age, address, *args, **kwargs):
        self.age = age
        self.address = address
        super().__init__(*args, **kwargs)


class Rent(ABC):
    def __init__(self, fixed_amount, monthly_amount):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount

    @abstractmethod
    def show_baner(self):
        pass


class Sale(ABC):
    def __init__(self, fee):
        self.fee = fee
    
    @abstractmethod
    def show_baner(self):
        return 'show baner'


class ApartmentRent(Apartment, Rent):
    def __str__(self):
        return f"{self.floor} {self.fixed_amount}"

    def show_baner(self):
        return 'show baner rent'


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"{self.floor} {self.fee}"

    def show_baner(self):
        return 'show baner sale'


class HouseRent(House, Rent):
    def __str__(self):
        return f"{self.address} {self.fixed_amount}"
    
    def show_baner(self):
        return 'show baner rent house'


class HouseSale(House, Sale):
    def __str__(self):
        return f"{self.address}, {self.fee}"
    
    def show_baner(self):
        return 'show baner sale house'


if __name__ == "__main__":
    # e = E()
    # print(E.mro())
    # e.greeting()

    estates = list()

    apartment_rent = ApartmentRent(floor=2, elevator=True, fixed_amount=120000000, monthly_amount=1000000)
    estates.append(apartment_rent)

    apartment_sale = ApartmentSale(floor=2, elevator=True, fee=120000000)
    estates.append(apartment_sale)


    hous_rent = HouseRent(age=20, address='Lorem ipsum', fixed_amount=120000000, monthly_amount=1000000)
    estates.append(hous_rent)

    hous_sale = HouseSale(age=20, address='Lorem ipsum', fee=16000000)
    estates.append(hous_sale)
    
    for e in estates:
        print(e.show_baner())

    # rent = Rent(floor=2, elevator=True, fixed_amount=120000000) # Error
    