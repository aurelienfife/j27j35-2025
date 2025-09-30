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
# Appending
# Insertion
# Deletion

def main():
    # Linked list creation = create the new node
    # The first node IS the list
    head = Node(10)
    print()


if __name__ == "__main__":
    main()
