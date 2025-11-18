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

for v in test_data:
    root = level_order_insert(root, v)
    

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

def print_tree(root):
    if not root:
        print("<empty>")
        return

    # Collect nodes level by level
    levels = []
    queue = [(root, 0)]
    max_width = 0
    while queue:
        node, level = queue.pop(0)
        if len(levels) <= level:
            levels.append([])
        if node:
            levels[level].append(node.value)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        else:
            levels[level].append(None)
            queue.append((None, level + 1))
            queue.append((None, level + 1))
        # Stop if the last level is all None (no more nodes)
        if level > 0 and all(n is None for n in levels[level]):
            levels.pop()
            break

    # Calculate width for centering
    max_nodes = 2 ** (len(levels) - 1)
    max_width = max_nodes * 3

    for i, level in enumerate(levels):
        spacing = max_width // (2 ** i + 1)
        line = ""
        connectors = ""
        for j, val in enumerate(level):
            node_str = " " if val is None else str(val)
            line += node_str.center(spacing)
            # Draw connectors except for the last level
            if i < len(levels) - 1:
                if val is not None:
                    left = "/" if levels[i+1][2*j] is not None else " "
                    right = "\\" if levels[i+1][2*j+1] is not None else " "
                else:
                    left = right = " "
                connectors += left + " " * (spacing - 2) + right + " " * (spacing - 2)
        print(line.center(max_width))
        if connectors.strip():
            print(connectors.center(max_width))

print_tree(root)