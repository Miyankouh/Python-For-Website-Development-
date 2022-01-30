from abstractfactory2 import Rugs 

class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate
    
    def exchange(self, product):
        return self.rate * product._price


if __name__ == "__main__":
    r1 = Rugs('persion rugs', 20)
    r2 = Rugs('Nain rugs', 22)
    r3 = Rugs('Morroco rugs', 24)

    adapter = PriceAdapter(rate=20000)

    rugs = [r1, r2, r3]

    for rug in rugs:
        print(f"{rug._name}: {adapter.exchange(rug)}")