# Binary Search tree - optimised for search

# Same nodes
class BSTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Same traversal methods
# in order: left, node, right
def in_order(node):
    # if node not empty
    if node:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)

def pre_order(node):
    if node:
        print(node.value, end=" ")
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end=" ")

# Insert (binary search tree)
# How it works:

# Start at the root node.
# Compare each node:
# Is the value lower? Go left.
# Is the value higher? Go right.
# Continue to compare nodes with the new value
# until there is no right or left to compare with.
# That is where the new node is inserted.

def insert_bst(root, v):
    # Scenario 1: tree is empty
    if root is None:
        root = BSTreeNode(v)
        return root
    # Scenario 2: value already in tree
    if root.value == v:
        return root

    # Otherwise compare recursively
    if v > root.value:
        root.right = insert_bst(root.right, v)
        return root
    else:
        root.left = insert_bst(root.left, v)
        return root


def find_bst(root, v):

    if root is None:
        return None
    
    if root.value == v:
        return root
    
    if v > root.value:
        return find_bst(root.right, v)
    else:
        return find_bst(root.left, v)
    


test_data = [13, 7, 69, 2, 21, 49, 3]

root = None
for n in test_data:
    root = insert_bst(root, n)

in_order(root)


# Same (generated) print
def print_tree(node, indent="", last=True):
    if node:
        print_tree(node.right, indent + ("   " if last else "│  "), False)
        print(indent + ("└── " if last else "┌── ") + str(node.value))
        print_tree(node.left, indent + ("   " if last else "│  "), True)

print_tree(root)
