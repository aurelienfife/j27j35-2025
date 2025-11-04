import stack_aa, queue_aa

'''
Algorithm with 2 stacks:
    - Complexity O(n)
    - Requires twice the memory

    - Push all the elements in stack 1
    - Create empty stack - stack 2
    - For each element in stack 1 - pop
    - push element into stack 2

    Replace empty stack 1 with new stack 2
'''

def invert_stack(some_stack):
    # Create a new stack
    new_stack = stack_aa.Stack()
    
    # while stack not empty
    # pop element and push to other stack
    while not some_stack.isEmpty():
        e = some_stack.pop()
        print(e, "popped from stack 1 and pushed to stack 2")
        new_stack.push(e)
        # For debug
    
    return new_stack


def main():
    
    sample_data = ["DME L5", "P&E", "Python1", "Python2", "P&E"]
    s = stack_aa.Stack()

    # Insert all the sample data to the stack
    for e in sample_data:
        s.push(e)
        print(e, "pushed to stack 1")
    
    # Test the inversion
    s = invert_stack(s)

    print("Final stack 2")
    while not s.isEmpty():
        print(s.pop())
    
    pass

if __name__ == "__main__":
    main()