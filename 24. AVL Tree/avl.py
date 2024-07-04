
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
 
import queue

#* Creating AVL
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrder(rootNode):                    #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return
    print(rootNode.data)                             # ------------> TC = O(1)
    preOrder(rootNode.leftChild)                     # ------------> TC = O(n/2)
    preOrder(rootNode.rightChild)                    # ------------> TC = O(n/2)

def inOrder(rootNode):                     #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return
    inOrder(rootNode.leftChild)                      # ------------> TC = O(n/2)
    print(rootNode.data)                             # ------------> TC = O(1)
    inOrder(rootNode.rightChild)                     # ------------> TC = O(n/2)

def postOrder(rootNode):                   #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return
    postOrder(rootNode.leftChild)                    # ------------> TC = O(n/2)
    postOrder(rootNode.rightChild)                   # ------------> TC = O(n/2)
    print(rootNode.data)                             # ------------> TC = O(1)

def levelOrder(rootNode):                  #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return
    else:
        customeQueue = queue.Queue()
        customeQueue.put(rootNode)
        while not (customeQueue.empty()):
            root = customeQueue.get()
            print(root.data)
            if root.leftChild is not None:
                customeQueue.put(root.leftChild)
            if root.rightChild is not None:
                customeQueue.put(root.rightChild)

def searchNode(rootNode, nodeValue): #! ------------> TC = O(logN), SC = O(logN)
    if rootNode is None or rootNode.data is None:
        return "Node not found"
    if rootNode.data == nodeValue:
        return "Value is Found"
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None and rootNode.leftChild.data == nodeValue:
            return "Value found on Left"
        else:
            return searchNode(rootNode.leftChild, rootNode)
    else:
        if rootNode.rightChild is not None and rootNode.rightChild.data == nodeValue:
            return "Value found on Right"
        else:
            return searchNode(rootNode.rightChild, rootNode)


newAVL = AVLNode(10)                        # ------------> TC = O(1), SC = O(1)