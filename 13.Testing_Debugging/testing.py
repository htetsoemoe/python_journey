# import the unittest module
import unittest

# The functions/classes to be tested
def add_numbers(a, b):
    return a + b
    # return a + b + 1

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divided by 0")
    return a / b

# Creating The Test Case Class
class TestMathFunctions(unittest.TestCase): # Inherit from unittest.TestCase
    # Test Methods (must start with test_)
    """Test if the addition of the add_numbers function is correct"""
    def test_add(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract(self):
        """Tests if the subtraction of the subtract_numbers function is correct."""
        self.assertEqual(subtract_numbers(5, 2), 3)
        self.assertEqual(subtract_numbers(2, 5), -3)
        self.assertEqual(subtract_numbers(10, 0), 10)

    def test_multiply(self):
        """Tests if the multiplication of the multiply_numbers function is correct."""
        self.assertEqual(multiply_numbers(2, 4), 8)
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_divide(self):
        """Tests if the division of the divide_numbers function is correct."""
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertAlmostEqual(divide_numbers(10, 3), 3.333333, places=6) # for floating point numbers

        # Test if an error is raised when dividing by 0
        with self.assertRaises(ZeroDivisionError): # This code should raise a ZeroDivisionError
            divide_numbers(10, 0)

        # Test if a TypeError is raised with a different data type
        with self.assertRaises(TypeError):
            divide_numbers("a", 2)


# To run the tests
if __name__ == '__main__':
    unittest.main()