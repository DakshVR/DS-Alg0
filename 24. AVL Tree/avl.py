
#* What is an Avl tree?
#  AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of the left and right subtrees cannot be more than one for all the nodes.

# All properties of BST applies to AVL.
# Additional property, the tree must be balanced, making BST balanced.

# If at any time heights of left and right subtree differ by more than one, then rebalancing is done to restore AVL propery, this process is called ROTATION.

#* Why we need Avl tree?
# Time complexity is O(LogN), faster insertion, deletion and searching.
# It takes less time to traverse through Balanced tree than BST which formed with 10,20,30,40,50,60,70 or similar data.

#! Common Operations on AVL
#* Creation of AVL trees,

# newAVL = AVL()
# 
# rootnode = None
# leftchild = None
# rightchild = None

# Search for a node in AVL trees
# Traverse all nodes in AVL trees
# Insert a node in AVL trees
# Delete a node from AVL trees
# Delete entire AVL trees
 

#* Creating AVL
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

newAVL = AVLNode(10)                        # ------------> TC = O(1), SC = O(1)