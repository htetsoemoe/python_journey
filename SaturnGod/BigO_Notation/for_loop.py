import time

def sum_of_n(n):
    start_time = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end_time = time.time()
    return the_sum,end_time - start_time

for i in range(5):
    print("Sum is %d, %.7f seconds" % sum_of_n(100000))

"""
Sum is 5000050000, 0.0033994 seconds
Sum is 5000050000, 0.0029254 seconds
Sum is 5000050000, 0.0029459 seconds
Sum is 5000050000, 0.0045314 seconds
Sum is 5000050000, 0.0048859 seconds
"""
