from stack import Stack

def divideBy2(decNumber):
    print(f"Decimal: {decNumber}")

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString

print(f"Binary: {divideBy2(668)}") 

# 668/2 = 334 , Mod : 0
# 334/2 = 167,  Mod: 0
# 167/2 = 83,   Mod: 1
# 83/2 = 41,    Mod: 1
# 41/2 = 20,    Mod: 1
# 20/2 = 10,    Mod: 0
# 10/2 = 5,     Mod: 0
# 5/2 =  2,     Mod: 1
# 2/2 = 1,      Mod: 0
# 1/2 = 0,      Mod: 1

# In Stack: [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
# Binary: 1010011100