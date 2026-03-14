#Abstract class = A class that cannot be instantiated on its own;
#   ;Meant to be subClassed - They must be parents to children classes.
#They can contain abstract methods, which are declared but have no implementation.
#       Benefits of Abstract classes
#       1. Prevents instantiation of the class itself = We cannot create an object from a class that is abstract
#       2. Requires children to use inherited abstract methods.;

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")

boat = Boat()

boat.go()
boat.stop()

