# 1. Accessing Instance Variables
# 2. Without self (Class Variables)
class Circle:
    # Class variable - shared by all instances
    pi = 3.14159

    def __init__(self, radius):
        # Instance variable - unique to each instance
        self.radius = radius

    def area(self): 
        # Access class variable using class name
        return Circle.pi * self.radius ** 2
    
    def circumference(self):
        # Access class variable using self (also work)
        return self.pi * 2 * self.radius
    
circle1 = Circle(5)
print(f"circle1 area: {circle1.area()}")
print(f"circle1 circumference: {circle1.circumference()}")

circle2 = Circle(10)
print(f"circle2 area: {circle2.area()}")
print(f"circle2 circumference: {circle2.circumference()}")