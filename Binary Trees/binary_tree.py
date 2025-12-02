# Basic binary tree - Node
# Unsorted - using level-order insertion

class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


# Level-order insertion
# (top to bottom, left to right)
def level_order_insert(root, value):
    if root is None:
        return BTreeNode(value)
    # If root is not none queue element
    queue = [root]

    # While elements are in the queue
    # Dequeue the first available node
    while queue:
        node = queue.pop(0)

        # If left or right are available
        # Create new node there and end
        # Otherwise send left / right to queue and continue

        if node.left is None:
            node.left = BTreeNode(value)
            break
        else:
            queue.append(node.left)
        
        if node.right is None:
            node.right = BTreeNode(value)
            break
        else:
            queue.append(node.right)

    # Return the tree's root 
    return root




# Delete node: deepest
def delete_deepest(root):
    pass

# Delete node: value
def delete_node(root, key):

    # Tree is empty = return empty tree
    if root is None:
        return None
    
    # If tree is single-node
    # delete node if match and return empty tree
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
        
    # More than one node -> need to search
    # Creating a queue (for traversal)
    # And two variables to track current node
    # And node needing deleted
    queue = [root]
    current = None
    key_node = None

    # While the queue is not empty
    while queue:
        # Current position is dequeued element
        current = queue.pop(0)

        # Check if element is found
        if current.data == key:
            key_node = current
        
        # If left and right have a value (not None)
        # queue them
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    # When we run this loop, we keep track of the current element
    # Which means that once the loop has run its course (queue is empty)
    # 'current' will contain the deepest node (bottom-most and right-most)

    # If we found key_node = replace the data with 
    # data of current_node
    if key_node is not None:

        v = current.data
        key_node.data = v

        # Delete the deepest node
        # Another function
        delete_deepest(root)

    return root















# Level-order delete
# Remove value from tree
# Replace with value from deepest node



test_data = ['R', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
root = None

for v in test_data:
    root = level_order_insert(root, v)
    

def print_tree(node, indent="", last=True):
    if node:
        print_tree(node.right, indent + ("   " if last else "│  "), False)
        print(indent + ("└── " if last else "┌── ") + str(node.value))
        print_tree(node.left, indent + ("   " if last else "│  "), True)

print_tree(root)

# BST insertion
# (left < node < right)

# root = BTreeNode('R')
# nodeA = BTreeNode('A')
# nodeB = BTreeNode('B')
# nodeC = BTreeNode('C')
# nodeD = BTreeNode('D')
# nodeE = BTreeNode('E')
# nodeF = BTreeNode('F')
# nodeG = BTreeNode('G')

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

# in_order(root)
# print()
# pre_order(root)
# print()
# post_order(root)
# print()

