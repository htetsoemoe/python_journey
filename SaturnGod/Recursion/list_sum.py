def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])
    
print(listsum([1,2,5,9,7]))

# Looping from top to down
# 1,2,5,9,7

# 1     +       2,5,9,7
# 2     +       5,9,7
# 5     +       9,7
# 9     +       7
# 7


# Calculate from bottom to top
# 24

# 1     +       23
# 2     +       21
# 5     +       16
# 9     +       7
# 7