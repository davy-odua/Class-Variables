#Multilevel inheritance = Where a class inherits attributes and methods from a class which inherits from another class.
#                       Think of a grandparent , parent and child relationship. - The Grand child inherits traits
#                       from the parent who also inherits traits from the grandparent.
#                       C(B) <- B(A) <- A

#Multiple inheritance = Where a child from inherits from more than one parent class.
#                       C(A, B)



#inheritance = Where a class inherits from another class.

class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animals):
    pass

class Cat(Animals):
    pass

class Mouse(Animals):
    pass

dog = Dog("Boss")
cat = Cat("Messi")
mouse = Mouse("Leo")

print(dog.name)
print(cat.name)
print(mouse.name)

mouse.sleep()
mouse.eat()




##multipleinheritance and multilevel inheritance.
##multiple inheritance = C(A, B)

class Animal:
    def __init__(self, name):
        self.name = name


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey, Predator):
    pass


hawk = Hawk("Hawk")
rabbit = Rabbit("Rabbit")
fish = Fish("Fish")

hawk.hunt()
rabbit.flee()
fish.flee()
fish.hunt()

































































