#Variables.
# class variables = Are variables that are shared by all objects in the class.
#Class variables are defined out-side of the constructor
#Class variables allow you to share data among all objects created from the class
#while instance variables - each object has their own version
#instance variables = Are defined in-side of the constructor.
#

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self,name, age ):   #CONSTRUCTOR
        self.name = name  #instance variables
        self.age = age
        Student.num_students += 1

student11 = Student("Spongebob", 35)
student22 = Student("Patrick", 33)
student33 = Student("Square", 55)
student44 = Student("Sandy", 27 )

print(student22.name)
print(student22.age)
print(Student.class_year)  #Its good practice to access the class variable by the class name itself and not any instance of the class
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student11.name)
print(student22.name)
print(student33.name)
print(student44.name)





























# class University:
#
#     year = 2025
#     students_no = 0
#
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
#         University.students_no += 1
#
#     def grad(self):
#         print(f"Many students pursuing {self.course} will graduate this {self.year}. ")
#         print(f"{University.students_no} students will graduate this {University.year} ")
#
#
# student1 = University("Kevin", "BACHIT")
# student2 = University("Dominic", "BACHCOMMERCE")
# student3 = University("James", "BACHENGINEERING")
#
# student1.grad()
# print(f"{student1.name} - {student1.course}")
# print(f"{student2.name} - { student2.course}")
# print(f"{student3.name} - {student3.course}")
#
# print(University.students_no)
# print(University.year)
#






