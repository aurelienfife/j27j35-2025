# Queue (left to right)
# Using a linked-list type node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Enqueue
def push(s, value):
    # if the the queue is empty
    n = Node(value)
    if s == None:
        s = n
    else: # Until q has a next element, traverse
        while s.next:
            s = s.next
        # Once last element reached, add new one
        s.next = n
