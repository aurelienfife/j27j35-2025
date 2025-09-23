# Recursive quicksort on array
def quicksort(arr):

    # Base case 1 - if array is 1 element
    # Return itself
    if len(arr) <= 1:
        return arr
    else:
        # In this case create a pivot point
        # and two empty lists
        pivot = arr[-1]
        left = []
        right = []

        # All elements in list minus last
        for e in arr[:-1]:
            # If less -> left
            # If more -> right
            if e <= pivot:
                left.append(e)
            else:
                right.append(e)
        
        return quicksort(left) + [pivot] + quicksort(right)

# Test data
data = [3,7,10,5,1,8]
sorted = quicksort(data)
print(sorted)

