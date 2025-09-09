import array
import datetime

def bubble_sort(arr):
    # Counting
    swap_count = 0
    pass_count = 0
    
    n = len(arr)
    for i in range(n):
        pass_count += 1
        for j in range(n - 1):
            pass_count += 1
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

    print(f"Total passes: {pass_count}, Total swaps: {swap_count}")

# 'i' indicates an array of integers
# Types can be found in the array module documentation
numbers = array.array('i', [34, 7, 23, 32, 5, 62, 78, 1, 45, 19])

# Timestamp before sorting
t = datetime.datetime.now()      

bubble_sort(numbers)

t2 = datetime.datetime.now()
print(f"Time taken: {t2 - t}")

print(numbers)


