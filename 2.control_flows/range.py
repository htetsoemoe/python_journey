five_to_ten = list(range(5, 10))
zero_to_ten_step = list(range(0, 10, 3)) # 3 is the `step`
minus_with_step = list(range(-10, -100, -30)) # -30 is the `step`

print(five_to_ten)
print(zero_to_ten_step)
print(minus_with_step)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])