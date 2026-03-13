#Inheritance = Allows a class to inherit the attributes and methods from another class.
#             Helps with code reusability and extensibility.
#             class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
         print(f"{self.name} is eating")
    def sleep(self):
         print(f"{self.name} is asleep")


class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")


class Mouse(Animal):
    def speak(self):
        print("SQUECK")

dog = Dog("Bosco")
cat = Cat("Miyau")
mouse = Mouse("Mickey")

print(mouse.name)
print(mouse.is_alive)

mouse.eat()
dog.sleep()
cat.speak()



























