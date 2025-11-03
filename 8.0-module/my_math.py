#my_math.py
PI = 3.14159

def add(a, b):
    """Doc_String: Add two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtract"""
    return a - b

def multiply(a, b):
    """Multiply"""
    return a * b

def divide(a, b):
    """Divide"""
    if b == 0:
        print("Error: Cannot be divided by 0")
        return None
    return a / b

def circle_area(radius):
    """Calculate area of a circle"""
    return PI * (radius ** 2)

print("my_math.py module is loading...") # Appears this line, when a module is loading