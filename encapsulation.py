class Computer:
    def __init__(self):
        self.__price = 1000
    def sell(self):
        print("The price of the computer is {}.".format(self.__price))
    def changeprice(self, newprice):
        self.__price = newprice
computer = Computer()
computer.sell()
computer.__price = 1300
computer.sell()
computer.changeprice(1400)
computer.sell()