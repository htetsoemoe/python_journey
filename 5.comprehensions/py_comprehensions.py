# [expression for item in collection]
my_squares = [x*x for x in range(100)]
print(my_squares)
print(f"______________________________")

# [expression for item in collection if condition]
my_even_squares = [x*x for x in range(100) if x % 2 == 0]
print(my_even_squares)
