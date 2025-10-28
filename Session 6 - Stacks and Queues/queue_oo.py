# Queue in Python - object oriented
# Based on array/linked list


# Linked list based version
# From geeksforgeeks

# Node for the linked list: class
# The node contains two members: data and next
class Node:
    def __init__(self, new_data):
       self.data = new_data
       self.next = None

# The Queue class
# Keep track of front, back and size
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.current_size = 0
        
            


# Quick example - with an array
class QueueA:     # A for array
    def __init__(self):     # Initialiser / constructor
        self.array = []   # List backing the queue
    
    # Methods to add data and dequeue data
    def enqueue(self, new_data):
        # Just a proxy to inserting data at index 0
        self.array.insert(0, new_data)

    def dequeue(self):
        # if list is empty return None
        if len(self.array) == 0:
            return None
        else:
            return self.array.pop()
 
# Just some test code
# Create a new queue
# Object name is q1, class is queueA
q1 = QueueA()

# Insert some data
q1.enqueue("test")
q1.enqueue("another test")
q1.enqueue("something")

print(q1.array)

print(q1.dequeue())
print(q1.dequeue())
