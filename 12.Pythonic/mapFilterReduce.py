print("\n--- Map, Filter, Reduce ---")
from functools import reduce

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map() to convert each number to a string
string_numbers = list(map(str, data))
print(f"String numbers: {string_numbers}")

# 2. Use filter() to select numbers greater than 5.
greater_than_5 = list(filter(lambda x: x > 5, data))
print(f"Numbers greater than 5: {greater_than_5}")

# 3. Use reduce() to multiply all numbers.
product_of_numbers = reduce(lambda x, y: x * y, data)
print(f"Product of numbers: {product_of_numbers}")