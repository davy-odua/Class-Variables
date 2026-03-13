
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model #Assiging the values to the parameters.
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"I have been driving a {self.model} since {self.year}")
    def stop(self):
        print(f"He had to stop driving  the {self.model} because its {self.color} color was fading away ")











class Campus:
    def __init__(self, name, location, main_courses, no_students):
        self.name = name
        self.location = location
        self.main_courses = main_courses
        self.no_students = no_students

    def information_(self):
        print(f" The {self.name} which is located in {self.location} offers numerous courses especially {self.main_courses} courses ")

    def contains(self):
        print(f" The main campus of {self.name} contains {self.no_students} students. Since it is located in {self.location} ")











