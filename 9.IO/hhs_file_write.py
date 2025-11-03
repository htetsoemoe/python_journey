print("--- Writing to files ---")

# 1. Create and write a new file with 'w' (write) mode
# If the file already exists, old data will be deleted and a new one will be created.
with open("greeting.txt", "w") as file_handle:
    file_handle.write("Hello from Python\n")
    file_handle.write("Practice makes perfect!\n")
    file_handle.write("Learning with doing a project.")
print("greeting.txt has been newly written.")

# 2. Append to the end of a file with 'a' (append) mode
# If the file already exists, it will not be deleted but new data will be added to the end.
with open("greeting.txt", 'a') as file_handle:
    file_handle.write("\nThe Zen of Python")
    file_handle.write("\nNumpy, Pandas, Scikit Learn")
print("greeting.txt has been appended with new data.")

# 3. Create a new file with 'x' (exclusive creation) mode
# An Error will occur if the file already exists.
try:
    with open("new_file_only.txt", 'x') as file_handle:
        file_handle.write("This file should only be created once.")
    print("new_file_only.txt was successfully created and written.")
except FileExistsError:
    print("Error: The new_file_only.txt file already exists. Cannot create a new one.")