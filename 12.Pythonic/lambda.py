print("\n--- Lambda Functions ---")

# 1. A Lambda Function to multiply two numbers
multiply_lambda = lambda x, y: x * y
print(f"10 * 5 = {multiply_lambda(10, 5)}")


# A Lambda Function to get the first character of a string
get_first_char = lambda s: s[0] if s else ""
print(f"The first character of 'Python' is: {get_first_char('Python')}")


# Sort a list of dictionaries based on their value
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 75},
    {"name": "Alice", "score": 95},
]
# Sort to show the highest score first (descending)
sorted_students = sorted(students, key= lambda student: student["score"], reverse=True)
print(f"Students sorted by score: {sorted_students}")