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


test_data = ['R', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
root = None

root=level_order_insert(root, 'R')


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

in_order(root)
print()
pre_order(root)
print()
post_order(root)
print()

