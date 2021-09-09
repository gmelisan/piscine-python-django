import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.served_count = 0
        self.broken = False

    class EmptyCup(HotBeverage):
        name = 'empty cup'
        price = 0.90
        def description(self):
            return 'An empty cup?!  Gimme my money back!'

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = 'This coffee machine has to be repaired.'

        def __str__(self):
            return self.message

    def repair(self):
        self.broken = False

    def serve(self, t):
        if self.broken:
            raise self.BrokenMachineException()
        self.served_count += 1
        if self.served_count == 11:
            self.broken = True
            self.served_count = 0
            raise self.BrokenMachineException()
        if random.random() < 0.3:
            return self.EmptyCup()
        else:
            return t()

def test():
    cm = CoffeeMachine()

    try:
        print(cm.serve(Coffee))
        print(cm.serve(Tea))
        print(cm.serve(Chocolate))
        print(cm.serve(Cappuccino))
        print(cm.serve(Coffee))
        print(cm.serve(Tea))
        print(cm.serve(Chocolate))
        print(cm.serve(Cappuccino))
        print(cm.serve(Coffee))
        print(cm.serve(Tea))
        print(cm.serve(Chocolate))
    except CoffeeMachine.BrokenMachineException as error:
        print(error)

    print('==== Repair ====')
    cm.repair()
    print(cm.serve(Coffee))
    print(cm.serve(Tea))

    try:
        print(cm.serve(Coffee))
        print(cm.serve(Tea))
        print(cm.serve(Chocolate))
        print(cm.serve(Cappuccino))
        print(cm.serve(Coffee))
        print(cm.serve(Tea))
        print(cm.serve(Chocolate))
        print(cm.serve(Cappuccino))
        print(cm.serve(Coffee))
        print(cm.serve(Tea))
        print(cm.serve(Chocolate))
    except CoffeeMachine.BrokenMachineException as error:
        print(error)
    
if __name__ =='__main__':
    test()

