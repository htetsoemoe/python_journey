def selection_sort(array):
    for num in range(len(array)):
        pos_of_min = num
        print(f"pos_of_min: {pos_of_min}")
        for loc in range(num,len(array)) :
            print(f"loc: {loc}")
            if array[loc] < array[pos_of_min]:
                pos_of_min = loc
        
        temp = array[num]
        array[num] = array[pos_of_min]
        array[pos_of_min] = temp
        
    return array

list = [1,20,31,444,8,9]
print(selection_sort(list))