# Create a dictionary for a book's information.
book = {
    "title": "Python Basic",
    "author": "Ko Python",
    "year": "2022",
    "pages": 550
}
print(f"Book information: {book}")

# Print the book's title and pages.
print(f"Book title: {book['title']}")
print(f"Number of pages: {book['pages']}")

# Change the book's author to "Ko Demo"
book["author"] = "Ko Demo"
print(f"After changing the author: {book}")

# Add a new key "genre" with the value "Programming"
book['genre'] = "Programming"
print(f"After adding genre: {book}")


# len(), keys(), values(), items()
student = {
    "name": "Ko Demo",
    "age": 22,
    "city": "Mandalay"
}

print(f"len(): {len(student)}")
print(f"keys(): {student.keys()}") # keys(): dict_keys(['name', 'age', 'city'])
print(f"values(): {student.values()}") # values(): dict_values(['Ko Demo', 22, 'Mandalay'])
print(f"items(): {student.items()}") #  dict_items([('name', 'Ko Demo'), ('age', 22), ('city', 'Mandalay')])

# Iterating with a for loop
print('\n--- Iterating through Dictionary Items ---')
for key, value in student.items():
    print(f"{key}: {value}")

# .get(key, default_value)
person = {"name": "Ko Demo"}
print(person.get("name"))
print(person.get("age", "Unknown"))