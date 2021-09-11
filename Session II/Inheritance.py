class Car:
    def __init__(self):
        print("hey I am the parent car")

    def whoami(self):
        print("I am a car")

    def whatdoido(self):
        print("I help you to ride")


class Tesla(Car):
    def __init__(self):
        super().__init__()
        print("hey I am the child car tesla")

    def whoami(self):
        super().whoami()
        print("i am the tesla")

    def whatdoidont(self):
        print("dude I can't fly")    
    

my_tesla = Tesla()
my_tesla.whoami()
my_tesla.whatdoido()
my_tesla.whatdoidont()