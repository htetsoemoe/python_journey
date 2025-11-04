print("\n--- Working with File Paths ---")

# Reading users.txt from the data folder
try:
    with open("data/users.txt", "r") as user_file:
        print("\n>>> Users from data/users.txt <<<")
        for user in user_file:
            print(user.strip())
except FileNotFoundError:
    print("Error: The data/users.txt file was not found.")