import array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 'i' indicates an array of integers
# Types can be found in the array module documentation
numbers = array.array('i', [34, 7, 23, 32, 5, 62, 78, 1, 45, 19])  

bubble_sort(numbers)
print(numbers)


