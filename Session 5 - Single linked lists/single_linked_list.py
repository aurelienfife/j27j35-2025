# Node class
# We'll use it in several instances, so worth having
# Node for single linked list

# Node class
# With value and reference to next element
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Traversal/print
# The traversal - based on a while loop
# While there is a next element, keep going
def print_list(first_node):
    current_node = first_node
    # Display the value
    print(current_node.value)
    # While there's something in "next", loop through and print
    while current_node.next != None: # if there's something in "next"
        # next becomes current
        current_node = current_node.next
        # display content
        print(current_node.value)
        

# Appending
# Insertion
# Deletion

def main():
    # Linked list creation = create the new node
    # The first node IS the list
    head = Node(10)
    print_list(head)


if __name__ == "__main__":
    main()
