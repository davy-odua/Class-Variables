from main import Car

#We are learning about Classes, Objects and methods
#An object is an instance of a class
# An object has attributes(variables) and methods(functions)
#Attributes are the components of an object or what the object is composed of.
#Example of an attribute. If a phone is an object the phone_number is its attribute.
#Methods (functions) is what the object can do.
#Example of a method. If a phone is the object the making_a_call is a method


#CREATING AN OBJECT




car1 = Car("BMW", 2025, "Black", False)
car2 = Car("NOAH", 2026, "white", True)
car3 = Car("Benz", 2026, "black", True)

print(car1.model, car1.year, car1.color, car1.for_sale)
print(car2.model, car2.year, car2.color, car2.for_sale)
print(car3.model, car3.year, car3.color, car1.for_sale)

car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()




















