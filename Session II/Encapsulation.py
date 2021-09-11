class Encapsulation:
    def __init__(self):
        self.__my_price = 10

    def sell(self):
        print("my selling price is {}".format(self.__my_price))

    def setprice(self, price):
        self.__my_price = price

encap = Encapsulation()
encap.sell()
encap.__my_price = 20
encap.sell()
encap.setprice(20)
encap.sell()