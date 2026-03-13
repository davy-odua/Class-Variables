#Creating an Object called Campus which consists of information concerning student , their universities and theirs details.
#Step 1 = To create the class. We must create a class first before we create the object because an object is an instance of a class
#Step 2 = Create the object inside the class
#Step 3 = Define parameters in the object.
#Step 4 = Assign attributes to parameters
#Step 5 = Define the Methods in the object
from main import Campus


campus1 = Campus("TUK", "CBD", "TECHNICAL", 18000)
campus2 = Campus("UON", "NAIROBI", "APPLIED_SCIENCES", 30000)
campus3 = Campus("KU", "THIKA", "SOCIAL_SCIENCES", 40000)

print(campus1.name, campus1.location, campus1.main_courses, campus1.no_students)
print(campus2.name, campus2.location, campus2.main_courses, campus2.no_students)
print(campus3.name, campus3.location, campus3.main_courses, campus3.no_students)

campus1.information_()
campus1.contains()
campus2.information_()
campus2.contains()
campus3.information_()
campus3.contains()


