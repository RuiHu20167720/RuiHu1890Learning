import math
# Create a circle class
# Data attributes: radius <- private
# property called radius which returns current radius
# setter called radius which allows you to set a radius > 0
# method get_area
class Circle:
    def __init__(self, radius:float):
        self.__radius = radius
    def area(self):
        area = math.pi * self.__radius**2
        return area
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Radius should greater than 0")
circle = Circle(1.0)
print(circle.area())
