# Queue (left to right)
# Using a linked-list type node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Enqueue
def enqueue(q, value):
    # if the the queue is empty
    n = Node(value)
    # Whether the queue is empty (none) or not, just set it as next
    n.next = q
    q = n
    return q

# Dequeue
def dequeue(q):
    head = q
    previous = None
    # Traverse the linked list
    while q.next:
        previous = q
        q = q.next

    # Save the value
    v = q.value
    # Delete the node
    previous.next = None
    # Return the value
    return v, head

# Peek
def peek(q):
    # Traverse the linked list
    while q.next:
        q = q.next

    return q.value

# isEmpty

# size

def main():
    # Reserves the name for the variable but assign nothing
    # Enqueue will do the job
    queue = None

    for p in ["Erik", "Jack", "Kadie", "Grant"]:
        queue = enqueue(queue, p)

    v, queue = dequeue(queue)
    print(v)
    v, queue = dequeue(queue)
    print(v)

    print()

if __name__ == "__main__":
    main()
