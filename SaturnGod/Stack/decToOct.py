from stack import Stack

def divideBy8(decNumber):
    print(f"Decimal: {decNumber}")

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 8
        remstack.push(rem)
        decNumber = decNumber // 8

    binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString

print(f"Binary: {divideBy8(668)}")

# Decimal: 668
# Binary: 1234