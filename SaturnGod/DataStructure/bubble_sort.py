def bubble_sort(array):
    exchange = True
    print(f"len(array): {len(array)}")
    num = len(array) - 1
    print(f"num: {num}")
    while num > 0 and exchange:
        exchange = False
        for i in range(num):
            print(f"num: {num}, i: {i}")
            if array[i] > array[i+1]:
                exchange = True
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        num = num - 1
    return array

# UNSORTED LIST
un_sorted_list = [3,1,2]
print(bubble_sort(un_sorted_list))

# SORTED LIST
# sorted_list = [1,2,3,4,8,9]
# print(bubble_sort(sorted_list))