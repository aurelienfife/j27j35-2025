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
    # Recursion: no need to worry about loops

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



root = BTreeNode('R')
nodeA = BTreeNode('A')
nodeB = BTreeNode('B')
nodeC = BTreeNode('C')
nodeD = BTreeNode('D')
nodeE = BTreeNode('E')
nodeF = BTreeNode('F')
nodeG = BTreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

in_order(root)
print()
pre_order(root)
print()
post_order(root)
print()

