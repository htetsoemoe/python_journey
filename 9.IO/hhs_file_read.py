# Reading the previously created greeting.txt
print("\n>>> Reading greeting.txt as a String with read() <<<")
with open("greeting.txt", "r") as f:
    content_all = f.read() # read the entire file as a String
    print(content_all)

print("\n>>> Reading greeting.txt line by line with readline() <<<")
with open("greeting.txt", "r") as f:
    print(f"First line: {f.readline().strip()}")
    print(f"Second line: {f.readline().strip()}")

print("\n>>> Reading greeting.txt as a List with readlines() <<<")
with open("greeting.txt", "r") as f:
    all_lines_list = f.readlines()
    for i, line in enumerate(all_lines_list): # enumerate() pairs the index with item
        print(f"Line {i + 1}: {line.strip()}")

print ("\n>>> Reading greeting.txt line by line with for loop (Best Method) <<<")
with open("greeting.txt", "r") as f:
    for line in f:
        print(f"Read line: {line.strip()}")


# Test what happens when a file does not exist
try:
    with open("non_existent_file.txt", "r") as f:
        print(f.read)
except FileNotFoundError:
    print("\nError: non_existent_file.txt file was not found.")