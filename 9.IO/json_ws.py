import json

# A Python Dictionary
user_data = {
    "name": "Jane Doe",
    "age": 30,
    "hobbies": ["reading", "hiking", "cooking"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "123456"
    }
}

# Writing a Python Dictionary to a JSON file
with open("user_profile.json", "w") as json_file:
    json.dump(user_data, json_file, indent=4) # indent=4 arranges to JSON to be more readable
print("\nuser_profile.json has been written.")

# Reading the data from the JSON file back into a Python Dictionary
with open("user_profile.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("\n--- Reading data back from user_profile.json ---")
    print(loaded_data)
    print(f"Loaded User Name: {loaded_data['name']}")
    print(f"Loaded User Hobbies: {loaded_data['hobbies']}")
    print(f"Loaded User street: {loaded_data['address']["street"]}")