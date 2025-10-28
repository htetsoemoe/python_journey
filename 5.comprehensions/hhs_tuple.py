print("\n--- Testing Tupels ---")
# Store a birth date (year, month, day) as a Tuple.
birthday = (1995, 7, 21)
print(f"My birthday: {birthday}")
print(f"Year: {birthday[0]}")
print(f"Day: {birthday[2]}")

# Try to change an item in the Tuple. (This will raise an error)
try:
    birthday[1] = 8
    print("This line will not printed.")
except TypeError as e:
    print(f"Error: Tuples cannot be modified. ({e})")


# Iterating through Tuples with a for loop
colors = ("red", "green", "blue")
print(f"\n--- Iterating through a Tuple ---")
for color in colors:
    print(color)