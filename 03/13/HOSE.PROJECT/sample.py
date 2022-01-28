from random import choice
from user import User
from estate import Apartment, House, Store
from region import Region
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent

FIRST_NAME = ['Ali', 'Reza', 'Mahdi']
LAST_NAME = ['Alavi', 'Razavi', 'Mahdvai']
MOBILES = ['09123456789', '09129876543', '09123459876', '09129873456', '09128765493']


def create_samples():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    reg1 = Region(name='R1')
    reg2 = Region(name='R2')
    apt1 = Apartment(
        has_elevator=True, has_parking=True, floor=2, user=User.objects_list[0],
        built_year=1393, region=reg1, area=80, rooms_count=2,
        address="Some text..."
    )

    house = House(
        has_yard=True, floors_count=1, user=User.objects_list[2], area=400,
        rooms_count=6, built_year=1370, region=reg1, address='Some text ...'
    )

    store = Store(
        user=User.objects_list[-1], area=30, rooms_count=0, built_year=1390,
        region=reg1, address="Some text ...."
    )

    # Create advertisment
    apartment_sell = ApartmentSell(
        has_elevator=True, has_parking=True, floor=2, user=User.objects_list[0],
        built_year=1393, region=reg1, area=80, rooms_count=2, convertable=False,
        address="Some text...", price_per_meter=10, discountable=True,
    )

    apartment_rent = ApartmentRent(
        has_elevator=True, has_parking=True, floor=2, user=User.objects_list[0],
        built_year=1393, region=reg1, area=80, rooms_count=2, convertable=False,
        initial_price=100, monthly_price=3.5, address="Some text...",
    )

    house_rent = HouseRent(
        has_yard=True, floors_count=1, user=User.objects_list[2], area=400,
        rooms_count=6, built_year=1370, region=reg1, address='Some text ...',
        initial_price=130, monthly_price=5.5, convertable=False
    )

    house_sell = HouseSell(
        has_yard=True, floors_count=1, user=User.objects_list[2], area=400,
        rooms_count=6, built_year=1370, region=reg1, address='Some text ...',
        price_per_meter=20, discountable=False, convertable=False
    )

    print("#" * 20, "\t samples created \t", "#" * 20)
