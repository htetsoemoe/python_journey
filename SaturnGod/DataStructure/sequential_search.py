def search(array, search_value):
    for (index, value) in enumerate(array): # return index and value
        if value == search_value:
            return index
    return -1

res = search([1,2,51,70,22,97,100,120], 97)
if res != -1:
    print("Found at index: ", res)
else:
    print("Not found")