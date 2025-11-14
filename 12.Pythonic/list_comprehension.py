# Example: Create a list of squares for numbers 1 to 10
squares_comp = [i * i for i in range(1, 11)]
print("List Comprehension")
print(f"square_comp: {squares_comp}")

# Example: List comprehension with if condition
even_squares = [i * i for i in range(1, 11) if i % 2 == 0]
print("List Comprehension with if condition")
print(f"even_squares: {even_squares}")

# Example: Create a list fo words with length greater than 4 characters
words = ["apple", "banana", "cat", "dog", "elephant"]
long_words = [word for word in words if len(word) > 4]
print(f"Long word: {long_words}")
