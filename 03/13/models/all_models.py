class User:

    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email

    def check_password(self, password):
        return self.password == password

    @classmethod
    def create(cls,  username, password, fullname, email):
        cls.validate_password(password)
        return cls(username, password, fullname, email)

    def __str__(self):
        return self.password

    @staticmethod
    def validate_password(password):
        if len(password) < 4:
            print("password should be more than 3 char")
            return False
        return True



class Customer(User):
    counter = 0  # class attrs

    def __init__(self, username, password, fullname, email):
        super().__init__(username, password, fullname, email)
        self.__wallet_amount = 0  # privet
        self._is_enable = False
        Customer.counter += 1

    def __str__(self):
        return self.username

    def set_enable(self):
        self.is_enable = True

    @property
    def wallet(self):  # convert method to the attr
        return self.__wallet_amount


class Reseller(User):

    def __init__(self, brand, logo, *args, **kwargs):
        self.brand = brand
        self.logo = logo
        super().__init__(*args, **kwargs)

    def check_password(self, password):
        print('Password login is not available')


class Product:
    product_list = list()

    def __init__(self, upc, name, price=0, description='', reseller=None):
        self.upc = upc
        self.name = name
        self.price = price
        self.description = description
        self.reseller = reseller
        Product.product_list.append(self)

    def __str__(self):
        return f"upc: {self.upc}\t name{self.name}"

    def is_free(self):
        return self.price == 0


