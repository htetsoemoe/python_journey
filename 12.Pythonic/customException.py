print("\n--- Custom Exceptions ---")

# 1. InvalidAgeError Custom Exception extends Exception Class
class InvalidAgeError(Exception):
    """Custom Exception for an invalid age."""
    def __init__(self, age, message="Age must be between 0 and 120."):
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_person_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    print(f"Age set to {age}.")

try:
    set_person_age(30)
    set_person_age(130)
except InvalidAgeError as e:
    print(f"Caught Custom Error: {e}")
except TypeError as e:
    print(f"Caught Type Error: {e}")
except Exception as e:
    print(f"Caught General Error: {e}")

try:
    set_person_age(-10)
except InvalidAgeError as e:
    print(f"Caught Custom Error: {e}")

try:
    set_person_age("fifty")
except TypeError as e:
    print(f"Caught Type Error: {e}")