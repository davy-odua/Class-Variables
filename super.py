#super() = A function used in a child class to call methods from a parent class (superclass)
#         Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius }cm^2 ")
        super().describe()

class Square(Shape):
    def __init__(self,color,filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width }cm^2 ")
        super().describe()

class Triangle(Shape):
    def __init__(self,color,filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.width * self.height }cm^2 ")
        super().describe()

circle = Circle("Red", True, 5)
square = Square("Yellow",False, 10 )
triangle = Triangle("Orange", True, 12, 15)

# print(f"The {circle.color} circle has a radius of {circle.radius}cm")
# print(f"The {triangle.color} triangle has a width of {triangle.width}cm and height of {triangle.height}cm")
# print(f"The {square.color} square has a width of {square.width}cm")


circle.describe()
triangle.describe()
square.describe()

