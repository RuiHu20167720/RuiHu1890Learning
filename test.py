import turtle


class Address:
    def __init__(self, street,city,state,postal_code,country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
my_address = Address(street="TerraNova",city="St. John's", state="NL",postal_code="A1B1G1",country= "CA")
print(my_address.city)
import math
from  turtle import *
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*self.radius*math.pi
    def draw(self):
        gary = turtle.Turtle()
        gary.pensize(5)
        gary.color("red")
        gary.circle(self.radius)
        turtle.done
test = Circle(10)
print(test.area() )
print(test.perimeter())
print(test.draw())
