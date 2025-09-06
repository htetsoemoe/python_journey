my_dict = {
    "name": "Alice",
    "age": 30
}

# Key exits, returns the value
name = my_dict.get("name")
print(f"Key exists, returns the value")
print(f"Name: {name}")

# Key does not exist, returns None (default behavior)
city = my_dict.get("city")
print(f"Key does not exist, returns None (default behavior)")
print(f"City: {city}")

# Key does not exist, returns a specified default value
country = my_dict.get("country", 0)
print("Key does not exist, returns a specified default value")
print(f"Country: {country}")