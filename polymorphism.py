#Polymorphism = Greek word that means "have many forms of faces"
#              Poly = Means "many"
#              Morphe = Form
from super import circle

#              TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as the parent class
#               2. "Duck typing" = Object must have necessary attributes/methods.
from abc import ABC, abstractmethod

class Shapes:

    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm^2")




































