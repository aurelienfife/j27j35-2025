# Queue in Python - object oriented
# Based on array/linked list

# Quick example - with an array

class queueA:     # A for array
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