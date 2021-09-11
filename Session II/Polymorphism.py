class Car:
    def my_job(self):
        print("dude, ride on me")

class Ship:
    def my_job(self):
        print("dude, sail on me")

class Rocket:
    def my_job(self):
        print("dude, fly on me")


def whatdoyoudo(vehicle):
    vehicle.my_job()


car = Car() 
#car.my_job()  

ship = Ship()
rocket = Rocket()

whatdoyoudo(car)
whatdoyoudo(ship)
whatdoyoudo(rocket)