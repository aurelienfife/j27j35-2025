from random import randint
import time

def createRandomData(numElements=20, maxNum=10):
    randomData = []
    for x in range(numElements):
        randomData.append(randint(0, maxNum))
    return randomData

def bubbleSort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break



print("Starting the sort process:")
rData = createRandomData(200,200)
#print("Unsorted data")
#print(rData)

start_time = time.time()
bubbleSort(rData)
end_time = time.time()

print("Bubble Sort time elapsed: " + str(end_time - start_time) + " seconds")
# print("Sorted data")
# print(rData)

print("Starting the sort process:")
rData = createRandomData(1000,1000)
#print("Unsorted data")
#print(rData)

start_time = time.time()
bubbleSort(rData)
end_time = time.time()

print("Bubble Sort time elapsed: " + str(end_time - start_time) + " seconds")
# print("Sorted data")
# print(rData)

print("Starting the sort process:")
rData = createRandomData(10000,10000)
#print("Unsorted data")
#print(rData)

start_time = time.time()
bubbleSort(rData)
end_time = time.time()

print("Bubble Sort time elapsed: " + str(end_time - start_time) + " seconds")
# print("Sorted data")
# print(rData)

print("Starting the sort process:")
rData = createRandomData(100000,100000)
#print("Unsorted data")
#print(rData)

start_time = time.time()
bubbleSort(rData)
end_time = time.time()

print("Bubble Sort time elapsed: " + str(end_time - start_time) + " seconds")
# print("Sorted data")
# print(rData)
