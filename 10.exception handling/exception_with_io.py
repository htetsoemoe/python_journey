print("\n--- try-except-else-finally ---")

def process_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(f"Completed reading contents form {filename}")
        processed_data = data.upper()
        return processed_data
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return None
    except Exception as e:
        print(f"There was an Error {e}")
        return None
    finally:
        print("File task has been finished.")


print("\n>>> Successful File Task <<<")
with open("greeting.txt", "w") as f:
    f.write("\nException Handling with I/O")
    f.write("\nPython is great!")
processed_result = process_data_from_file("greeting.txt")
if processed_result:
    print(f"Processed Data: {processed_result}")

print("\n>>> File not found <<<")
process_data_from_file("non_existent.txt")
    