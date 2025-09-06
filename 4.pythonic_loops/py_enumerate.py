from typing import List

fruits: List[str] = ["apple", "banana", "mango"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")