# A set of numbers
unique_numbers = {2, 2, 4, 4, 5, 8, 10}
print(unique_numbers) # the duplicate 2 and 4 are removed

vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)

print("Create set with set()")
created_set = set({1, 3, 5, 9})
print(f"created set: {created_set}")

print(f"add(), remove(), discard()")
hero_set = set()
hero_set.add("Iron Man")
hero_set.add("Bat Man")
hero_set.add("Iron Man")
print(hero_set)


my_set = {1, 2, 3, 4, 5}
my_set.remove(2) # my_set.remove(7) # KeyError: 5

my_set.discard(1)
my_set.discard(7) # 7 is not in the set, but no error

print(my_set)

print(f"union(), intersection(), difference()")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union: Union of two sets into a set (unique item)")
print(set1.union(set2))
print(set1 | set2)

print("Intersection: Get common items from two set")
print(set1.intersection(set2))
print(set1 & set2)

print("Difference: get items from set2 which include in set1")
print(set1.difference(set2))
print(set1 - set2)


clear_set = {"clear", "all"}
print(clear_set)
print(clear_set.clear())