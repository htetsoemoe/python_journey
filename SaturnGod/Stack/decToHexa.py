from stack import Stack

def divideBy16(decNumber):
    print(f"Decimal: {decNumber}")

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 16
        if rem == 10:
            remstack.push('A')
        elif rem == 11:
            remstack.push('B')
        elif rem == 12:
            remstack.push('C')
        elif rem == 13:
            remstack.push('D')
        elif rem == 14:
            remstack.push('E')
        elif rem == 15:
            remstack.push('F')
        else:
            remstack.push(rem)
        decNumber = decNumber // 16

    binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())
    return binString

print(f"Binary: {divideBy16(668)}")
    
# Decimal: 668
# Binary: 29C