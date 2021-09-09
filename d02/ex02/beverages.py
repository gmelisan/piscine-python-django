class HotBeverage:
    price = 0.30
    name = 'hot beverage'

    def description(self):
        return 'Just some hot water in a cup.'

    def __str__(self):
        s =  f'name : "{self.name}"\n'
        s += f'price : {self.price:.2f}\n'
        d = self.description()
        s += f'description : "{d}"\n'
        return s

class Coffee(HotBeverage):
    name = 'coffee'
    price = 0.40
    def description(self):
        return 'A coffee, to stay awake.'

class Tea(HotBeverage):
    name = 'tea'

class Chocolate(HotBeverage):
    name = 'chocolate'
    price = 0.50
    def description(self):
        return 'Chocolate, sweet chocolate...'

class Cappuccino(HotBeverage):
    name = 'cappuccino'
    price = 0.45
    def description(self):
        return 'Un po’ di Italia nella sua tazza!'


def test():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())

if __name__ =='__main__':
    test()
