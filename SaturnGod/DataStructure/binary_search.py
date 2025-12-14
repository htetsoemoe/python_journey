def binary_search(array, item):
    first = 0
    last = len(array) - 1
    while first <= last:
        mid = (first + last) // 2 # If get 3.5, but it will take 3
        mid_value = array[mid]
        print(f"MID_INDEX: {mid}, MID_VALUE: {mid_value}, FRIST_INDEX: {first}, LAST_INDEX: {last}")

        if mid_value == item:
            print(f"MID_VALUE: {mid_value} == SEARCH VALUE: {item}")
            return True
        else:
            if item < mid_value:
                last = mid - 1
                print(f"item: {item} < mid_value: {mid_value}, last (mid - 1): {last}")
            else:
                first = mid + 1
                print(f"item: {item} > mid_value: {mid_value}, first: {first}")

print(binary_search([8,14,18,20,26,66,78],18))
print(binary_search([8,14,18,20,26,66,78],19))                

