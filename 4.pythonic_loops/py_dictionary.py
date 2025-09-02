from typing import Dict

user: Dict[str, str] = {"name": "Alice", "email": "alice@mail.com"}
# for key in user:
#     print(key)

for value in user.values():
    print(value)    


# Iterate over key-value pairs (very common)
for key, value in user.items():
    print(f"{key}: {value}")

# Dictionary Comprehension (Similar to list comprehension) 
words = ['hello', 'world']
word_lengths = {word: len(word) for word in words}
print(word_lengths)