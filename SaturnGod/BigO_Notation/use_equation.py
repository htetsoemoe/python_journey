import time

def sum_of_n(n):
    start_time = time.time()
    the_sum = n * (n+1) / 2 # Instant of using equation reduces time and faster than using loop
    end_time = time.time()
    return the_sum, start_time - end_time

for i in range(5):
    print("Sum is %d, %.7f seconds" % sum_of_n(100000))

"""
Sum is 5000050000, 0.0000000 seconds
Sum is 5000050000, 0.0000000 seconds
Sum is 5000050000, 0.0000000 seconds
Sum is 5000050000, 0.0000000 seconds
Sum is 5000050000, 0.0000000 seconds
"""