# Example: Create a dictionary from a list of name (key: name, value: len(name))
names = ["Alice", "Bob", "Charlie", "David"]
name_length = {name: len(name) for name in names}
print(name_length)

numbers = [1, 2, 3, 4, 5, 6]
num_status= {num: "Event" if num % 2 == 0 else "Odd" for num in numbers}
print(num_status)


products = [("Laptop", 1200), ("Keyboard", 90), ("Mouse", 50)]
product_prices = {name: price for name, price in products}
print(f"Product prices: {product_prices}")


words = ["apple", "banana", "cherry"]
first_letters = {word: word[0] for word in words}
print(f"First letters: {first_letters}")
