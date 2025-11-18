import tkinter as tk
from tkinter import messagebox # to show pop-up messages

def on_button_click():
    """Function to be executed when the button was clicked"""
    user_name = name_entry.get() # Get the name form the Entry Box
    if user_name:
        greeting_label.config(text=f"Hello, {user_name}") # Change the text of the Label
        messagebox.showinfo("Greeting", f"Hello, {user_name}!") # Show a pop-up message
    else:
        messagebox.showwarning("Warning", "Please enter your name.")


# Create the Root Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x250") # Reduce the window size

# 1. Create a Label Widget (for the title)
title_label = tk.Label(root, text="Enter your name", font=("Arial", 16))
# The .pack() method automatically places the widgets on the window.
# It is convenient for simple application.
title_label.pack(pady=10) # pady = 10 adds 10 pixels of padding above and below the label

# 2. Create an Entry Widget (Text Box for the name input)
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

# 3. Create a Button Widget
greet_button = tk.Button(root, text="Greet", command=on_button_click, font=("Arial", 12))
greet_button.pack(pady=10)

# 4. Create a Label Widget (to display the greeting)
greeting_label = tk.Label(root, text="", font=("Arial", 14), fg="blue") # fg is foreground color
greeting_label.pack(pady=10)

# Start the Event Loop
root.mainloop()
print(f"Program exited!")


