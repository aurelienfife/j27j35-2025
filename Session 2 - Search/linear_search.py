# Linear search - including performance measurement
import datetime
import time

near_head = [7, 81, 14, 3, 94, 35, 31, 28, 17, 94, 13, 86, 94, 69, 11, 75, 54, 4, 3, 11, 27, 29, 64, 77, 62]
near_end = [90, 71, 25, 3, 11, 36, 45, 89, 63, 91, 66, 88, 70, 61, 74, 92, 96, 59, 84, 33, 30, 19, 41, 44, 7]
middle = [38, 93, 65, 97, 42, 39, 76, 87, 22, 73, 32, 60, 7, 98, 85, 40, 20, 26, 18, 95, 99, 12, 46, 10, 37]
not_in_list = [83, 50, 34, 48, 2, 16, 21, 8, 1, 5, 6, 9, 15, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 36]


# Linear search function
def linear_search(number, num_list):
    # Check elements 1 by 1
    for i in range(len(num_list)):
        
        # It's running too fast, I deliberately slow it down
        # to make the variance more obvious
        # time.sleep(0.001)
        # Leave commented out if not "testing"

        # If element at position matches term
        # return position
        if num_list[i] == number:
            return i
    # We return -1 to report that we have not found the value
    return -1

# Proxy function running the linear search but adding
# Performance stats
def measure_run(data_list): 
    # Take date/time before running
    before = datetime.datetime.now()
    result = linear_search(7, data_list)
    after = datetime.datetime.now()
    duration = after-before
    print("position: ", result, " duration: ", duration)

measure_run(near_head)
measure_run(near_head)
measure_run(near_end)
measure_run(middle)
measure_run(not_in_list)

