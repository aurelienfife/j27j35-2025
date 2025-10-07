# Some stack functions (non-OO)
def push(s, new_element):
    s.append(new_element)
    
def pop(s):
    return s.pop()

def peek(s):
    return s[-1]

def isEmpty(s):
    return len(s) == 0

def main():
    # The stack is a list, but we just use the functions above
    stack = []

    # Push
    push(stack, 'A')
    push(stack, 'B')
    push(stack, 'C')
    print("Stack: ", stack)
    # Pop
    element = pop(stack)
    print("Pop: ", element)
    # Peek
    topElement = peek(stack)
    print("Peek: ", topElement)
    # isEmpty
    print("isEmpty: ", isEmpty(stack))
    # Size
    print("Size: ",len(stack))

if __name__ == "__main__":
    main()
