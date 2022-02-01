class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Gateway:
    def __init__(self, name):
        self.name = name


class Payment:
    gateway = (Gateway('G1'), Gateway('G2'))
    def __init__(self, purchase):
        self.purchase = purchase
    

    def gat_gateway(self):
        return self.gateway[0] if self.purchase.total_price() < 100 else self.gateway[1]


    def pay(self):
        """ if payment amount is less than 100,
         use G1 gateway atherwise use G2  """
        gateway = self.gat_gateway()
        print(f"Payment is being paid though {gateway.name}")

class Purchase:
    def __init__(self):
        self.products = list()
        self.payment = Payment(self)

    def add(self, product):
        self.products.append(product)

    def total_price(self):
        return sum([p.price for p in self.products])

    def checkout(self):
        self.payment.pay()


if __name__ == '__main__':
    p1 = Product('P1',45)
    p2 = Product('P2',25)
    p3 = Product('P3',35)

    purchase = Purchase()
    purchase.add(p1)
    print(purchase.total_price())
    purchase.checkout()

    purchase.add(p2)
    print(purchase.total_price())
    purchase.checkout()

    purchase.add(p3)
    print(purchase.total_price())
    purchase.checkout()
    
