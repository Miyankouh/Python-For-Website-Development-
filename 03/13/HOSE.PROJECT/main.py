from random import choice
from user import User
from estate import Apartment, House, Store
from region import Region
from advertisment import ApartmentSell

FIRST_NAME = ['Nima', 'Siavash', 'Garsha']
LAST_NAME = ['Diar', 'Roostam', 'Saman']
MOBILE = ['0912456987', '09123665478', '09122548765', '09121234578', '09125478965']

if __name__ == '__main__':
    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.objects_list:
        print(f"{user.id}\t {user.fullname}")


    reg1 = Region(name="R1")
    apt1 = Apartment(
        has_elevator=True, has_parking=True, floor=2,user=User.objects_list[0],
        bulit_year=1394, region=reg1, area=80, rooms_count=2, 
        address="some text"
    )
    apt1.show_description()

    house = House(
        has_yard=True, floor_count=1, user=User.objects_list[2], area=400,
        rooms_count=4, bulit_year=1370, region=reg1, address="Some text ..."
    )
    house.show_description()

    store = Store(
        user=User.objects_list[-1], area=50, rooms_count=1, bulit_year=1399,
        region=reg1, address="Some text..."
    )
    store.show_description()

    # Create Advertisment
    apartment_sell = ApartmentSell(
        has_elevator=True, has_parking=True, floor=2,user=User.objects_list[0],
        bulit_year=1394, region=reg1, area=80, rooms_count=2, convertable=False,
        address="some text", price_per_meter=10, discountable=True,
    )
    apartment_sell.show_detail()
    