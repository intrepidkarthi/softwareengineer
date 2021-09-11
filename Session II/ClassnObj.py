class ClassnObj:

    my_word = "hello"

    def __init__(self):
        pass

    def my_method(self):
        print("hello")
    
    def __init__(self, model, color):
        self.model = model 
        self.color = color

my_first_car = ClassnObj("bmw", "black")
print(my_first_car.model)
print(my_first_car.color)
print(my_first_car.__class__.my_word)

my_second_car = ClassnObj("audi", "white")
print(my_second_car.model)
print(my_second_car.color) 
print(my_second_car.__class__.my_word)

 

