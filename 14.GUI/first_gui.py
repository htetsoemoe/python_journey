import tkinter as tk # import the tkinter module as tk

# 1. Create the Root Window (Main Window)
root = tk.Tk() # Creating a Tk() object gives us the root window

# 2. Set the title for the window
root.title("My First Tkinter App")

# 3. Set the size of the window (width x height)
root.geometry("400x300") # 400 pixels wide, 300 pixels high

# 4. Start the event loop
# The event loop keeps thw window open and waits for user events like clicks, keyboard inputs, etc.
root.mainloop()

print("Tkinter Application has closed.")

