# [expression for item in iterable if expression]

print("\n--- Testing List Comprehension ---")

all_fruits = ["apple", "banana", "apricot", "grape"]
a_fruits = [fruit for fruit in all_fruits if fruit.startswith("a")]
print(a_fruits)



# Create a list containing only even numbers from 1 to 20.
even_number = [num for num in range(1, 21) if num % 2 == 0]
print(f"Event numbers from 1 to 20: {even_number}")


# Create a new list with only uppercase words from a list of strings.
words = ["hello", "World", "PYTHON", "example"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")