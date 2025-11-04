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
    
    # Add the methods
    def isEmpty(self):
        return self.front is None
    
    # Add element
    def enqueue(self, new_data):
        # Create a new node
        new_node = Node(new_data)
        # If list is empty set back and front to node
        if self.isEmpty():
            self.front = self.back = new_node
        else:
        # Otherwise set the back's next to the new node
        # And the new node to the new back
            self.back.next = new_node
            self.back = new_node

        # Update size
        self.current_size += 1

    # Remove element from queue
    # If empty return None
    # Otherwise, return front element, after severing link
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            # Save the returned data to a variable
            returned_data = self.front.data
            # Set New front to next element
            self.front = self.front.next
            # If the new front is "None"
            if self.front is None:
                self.back = None
            self.current_size -= 1
            return returned_data
        
