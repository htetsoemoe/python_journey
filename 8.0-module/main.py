import my_math # my_math.py module ကို import လုပ်ခြင်း

print("\n--- Module Import လုပ်ပြီး အသုံးပြုခြင်း ---")

# Module ထဲက Function များကို ခေါ်ယူအသုံးပြုခြင်း (module_name.function_name)
result_add = my_math.add(10, 5)
print(f"10 + 5 = {result_add}")

result_sub = my_math.subtract(100, 30)
print(f"100 - 30 = {result_sub}")

result_mul = my_math.multiply(7, 8)
print(f"7 * 8 = {result_mul}")

result_div = my_math.divide(20, 4)
print(f"20 / 4 = {result_div}")

result_div_by_zero = my_math.divide(10, 0) # Error Message ပေါ်လာမယ်
print(f"10 / 0 = {result_div_by_zero}")

# Module ထဲက Variable ကို ဝင်ရောက်ကြည့်ခြင်း
print(f"Pi ရဲ့ တန်ဖိုး: {my_math.PI}")

# Module ထဲက function ကို PI variable နဲ့တွဲသုံးခြင်း
radius = 7
area = my_math.circle_area(radius)
print(f"အချင်းဝက် {radius} ရှိသော စက်ဝိုင်း၏ ဧရိယာ: {area:.2f}")


# from module_name import item1, item2, ...


print("\n--- Using Package Modules ---")

# Importing a module from a package (package_name.module_name)
import calculations.simple
import calculations.complex

sum_val = calculations.simple.add(50, 29)
print(f"Package simple.add: 50 + 29 = {sum_val}")

diff_val = calculations.simple.subtract(100 , 25)
print(f"Package simple.subtract: 100 - 25 = {diff_val}")

pow_val = calculations.complex.power(2, 5)
print(f"Package complex.power: 2^5 = {pow_val}")

sqrt_val = calculations.complex.sqrt(5)
print(f"Package complex.sqrt: sqrt(5) = {sqrt_val}")

# Importing specific functions directly
from calculations.simple import add as simple_add # For avoid name conflict
from calculations.complex import sqrt as complex_sqrt

print(f"Direct import simple_add: {simple_add(100, 11)}")
print(f"Direct import complex_sqrt: {complex_sqrt(100)}")

# math module (သင်္ချာဆိုင်ရာ လုပ်ဆောင်ချက်များ)
import math
print(f"PI (from math module): {math.pi}")
print(f"ceil(4.3): {math.ceil(4.3)}") # (5)
print(f"floor(4.9): {math.floor(4.9)}") # (4)
print(f"sin(0): {math.sin(0)}")

# random module (Random Values များ ထုတ်ပေးခြင်း)
import random
print(f"Random number (0.0 to 1.0): {random.random()}")
print(f"Random number (1 to 10): {random.randint(1, 10)}")
fruits_list = ["apple", "banana", "cherry", "durian"]
print(f"Random Fruit: {random.choice(fruits_list)}")

# datetime module (အချိန်နှင့် ရက်စွဲများ)
import datetime
current_time = datetime.datetime.now()
print(f"Current Time and Date: {current_time}")
print(f"Current Year: {current_time.year}")
print(f"Current Month: {current_time.month}")
print(f"Current Day: {current_time.day}")
# os module (Operating System လုပ်ဆောင်ချက်များ)
import os
print(f"Current Working Directory: {os.getcwd()}")
# os.mkdir("new_folder") # new_folder အမည်နဲ့ folder အသစ် ဖန်တီး
# os.remove("temp_file.txt") # temp_file.txt ကို ဖျက်
