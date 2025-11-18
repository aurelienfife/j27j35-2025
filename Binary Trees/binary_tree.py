# Basic binary tree - Node
# Unsorted - using level-order insertion

class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

