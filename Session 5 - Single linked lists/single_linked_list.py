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
def append(first_node, new_value):
    # Traverse until the end
    current_node = first_node
    while current_node.next != None:
        current_node = current_node.next
    # At the end of the loop, the current should have None as next
    # aka last node
    # create new node and link previous
    new_node = Node(new_value)
    current_node.next = new_node

# Insertion
# Deletion
def delete_value(first_node, value):
    # First, traverse in linear search mode
    # If no match, nothing happens
    # If match change the links
    current_node = first_node

    # Case if we have only one element and it is a match
    if current_node.value == value and current_node.next == None:
        current_node = None

    # Traverse
    while current_node.next != None:
        next_node = current_node.next

        # If the next node's value is what we want
        # Link current with next of next
        # Then void next
        if next_node.value == value:
            current_node.next = next_node.next
            next_node = None
            return # Exit the function
        
        # else just keep moving
        current_node = next_node


def main():
    # Linked list creation = create the new node
    # The first node IS the list
    head = Node(10)
    #print_list(head)

    # Append a few numbers
    append(head, 15)
    append(head, 20)
    append(head, 7)

    print_list(head)

    delete_value(head, 20)

    print_list(head)

if __name__ == "__main__":
    main()
