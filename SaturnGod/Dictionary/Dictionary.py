person1 = {'name': 'Alice', 'age': 27}
person2 = {'name': 'Bob', 'age': 28}

room = [person1, person2]

for person in room:
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print("=======")