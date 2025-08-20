print("Hello World from Python Program \n")


num = 7
flo = 7.9
str = "to be with you"
list_1 = [1, 2, 3, "a", "Yolo"] # Python lists are mutable
tuple_1 = (1, 2, 3, "a", "Yolo") # Python tuples are immutable

print("Number: ", num)
print("Floating Point:", flo)
print("String: ", str)
print("\n")

print("List: ", list_1, " >>> Python lists are mutable")
list_1[3] = "z"
list_1[4] = "Zolo"
print("List: ", list_1, " >>> Python lists are mutable \n")

print("Tuple: ", tuple_1, " >>> Python tuples are immutable")
print("Tuple index 2: ", tuple_1[2])
print("\n")

# Python Dictionaries
# In Python dictionary, Keys are immutable and Valuse are mutable.

print("In Python dictionary, Keys are immutable and Valuse are mutable.")
py_dict = {'name': 'James', 'address': 'Mars', 'phone': 100}
print("Dictionary: ", py_dict)

# To modify the values in dictionaries
py_dict['name'] = 'Bond'
print("py_dict['name']: ", py_dict['name'])