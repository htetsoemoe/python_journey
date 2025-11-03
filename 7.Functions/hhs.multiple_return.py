def get_user_info():
    name = "Alice"
    age = 25
    return name, age

print("Return multiple values as Tuple")
print(get_user_info())


print("\n--- Variable Scope ---")
# A Global Variable
app_version = "1.0.0"

def show_app_info():
   # Accessing the Global Variable inside the function
   print(f"App Version: {app_version}")

   # A Local Variable
   function_message = "This is a message inside the function."
   print(function_message)

show_app_info()

# Trying to access the Local Variable from outside the function. This will cause an error.
try:
   print(function_message)
except NameError as e:
   print(f"Error: {e} - function_message is in Local Scope.")

# Modifying a Global Variable from inside a function (using the global keyword)
total_users = 100 # Global Variable
def add_new_user(num_users):
   global total_users # Use the global keyword to modify the global variable
   total_users += num_users
   print(f"Total Users inside Function: {total_users}")

print(f"\nInitial Total Users: {total_users}")
add_new_user(5)
print(f"Final Total Users outside Function: {total_users}")