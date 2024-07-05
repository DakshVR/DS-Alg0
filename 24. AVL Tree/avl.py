
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
            return searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is not None and rootNode.rightChild.data == nodeValue:
            return "Value found on Right"
        else:
            return searchNode(rootNode.rightChild, nodeValue)
        
#! Insertion: 2 cases
#* Rotation is not required : Here it is same as BST
        #* ---> If value less than root node, go towards left
        #*  ---> Else go towards right
#* Rotation is required
        #* 4 conditions
        #? ----> Left Left (LL)   = Right Rotation from disbalanced node to grandchild
        #  Balance > 1, left is greater then right
        # Algorithm for LL
        # rotateright(DisbalancedNode):    #! ------------> TC = O(1), SC = O(1)
        #       newroot = Disbalanced.leftchild
        #       disbalancednode.left = disbalancednode.left.right
        #       newroot.right = disbalanced
        #       update height of disbalamced and newroot
        #       return newroot

        # ?----> Left Right (LR)
                # Step 1: rotate left disbalanced.leftchild
                # Step 2: rotate right disbalancedNode
        # Algorithm
        # rotateLeft(disbalancedNode):     #! ------------> TC = O(1), SC = O(1)
        #       newroot = disbalanced.rightchild
        #       disbalanced.right = disbalanced.right.left
        #       newroot.left = disbalanced
        #       update height of disbalamced and newroot
        #       return newroot

        # rotateright(DisbalancedNode):    #! ------------> TC = O(1), SC = O(1)
        #       newroot = Disbalanced.leftchild
        #       disbalancednode.left = disbalancednode.left.right
        #       newroot.right = disbalanced
        #       update height of disbalamced and newroot
        #       return newroot

        #? ----> Right Right (RR) = Left Rotation from disbalanced node to grandchild
        # Algorithm for RR
        # rotateleft(DisbalancedNode):     #! ------------> TC = O(1), SC = O(1)
        #       newroot = Disbalanced.rightchild 
        #       disbalancednode.rightchild = disbalancednode.right.left
        #       newroot.left = disbalanced
        #       update height of disbalamced and newroot
        #       return newroot

        #? ----> Right Left (RL)
                # Step 1: rotate right disbalanced.rightchild
                # Step 2: rotate left disbalancedNode
        # rotateright(DisbalancedNode):    #! ------------> TC = O(1), SC = O(1)
        #       newroot = Disbalanced.leftchild
        #       disbalancednode.left = disbalancednode.left.right
        #       newroot.right = disbalanced
        #       update height of disbalamced and newroot
        #       return newroot

        # rotateleft(DisbalancedNode):     #! ------------> TC = O(1), SC = O(1)
        #       newroot = Disbalanced.rightchild 
        #       disbalancednode.rightchild = disbalancednode.right.left
        #       newroot.left = disbalanced
        #       update height of disbalamced and newroot
        #       return newroot
        
def getHeight(rootNode):                   #! ------------> TC = O(1), SC = O(1)
    if not rootNode:
        return 0
    return rootNode.height

def rightRotation(DisbalancedNode):        #! ------------> TC = O(1), SC = O(1)
    newRoot = DisbalancedNode.leftChild
    DisbalancedNode.leftChild = DisbalancedNode.leftChild.rightChild
    newRoot.rightChild = DisbalancedNode
    DisbalancedNode.height = 1 + max(getHeight(DisbalancedNode.leftChild), getHeight(DisbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotation(DisbalancedNode):        #! ------------> TC = O(1), SC = O(1)
    newRoot = DisbalancedNode.rightChild
    DisbalancedNode.rightChild = DisbalancedNode.rightChild.leftChild
    newRoot.leftChild = DisbalancedNode
    DisbalancedNode.height = 1 + max(getHeight(DisbalancedNode.leftChild), getHeight(DisbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):                  #! ------------> TC = O(1), SC = O(1)
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):  #! ------------> TC = O(LogN), SC = O(LogN)
    if not rootNode:                                   # ------------> TC = O(1)
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:                 # ------------> TC = O(LogN)
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:                                           # ------------> TC = O(LogN)
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))                                       # ------------> TC = O(1)

    balance = getBalance(rootNode)                     # ------------> TC = O(1)

    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)                 # ------------> TC = O(1)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)                 # ------------> TC = O(1)
    
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)                  # ------------> TC = O(1)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)                  # ------------> TC = O(1)

    return rootNode


#! Deletion: 2 cases
#* Rotation is not required : 
        #* ---> Node to be deleted is Leaf node
                # find the node and delete

        #* ---> Node to be deleted has 1 child
                # Assign child to the nodes parent

        #* ---> Node to be deleted has 2 child
                # Find the successor, replace that with root
                # Child of successor becomes child of it's parents

#* Rotation is required
# Same as insertion, 4 conditions, LL, LR, RR, RL

def findSuccessor(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return findSuccessor(rootNode.leftChild)

def deleteNode(rootNode, nodeValue): #! ------------> TC = O(LogN), SC = O(LogN)
    if not rootNode:
        return rootNode                                # ------------> TC = O(1)
    elif nodeValue < rootNode.data:                 # ------------> TC = O(LogN)
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:                 # ------------> TC = O(LogN)
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:                 # ------------> TC = O(1)
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:              # ------------> TC = O(1)
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = findSuccessor(rootNode.rightChild)   # ------------> TC = O(LogN)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)       # ------------> TC = O(LogN)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))                                       # ------------> TC = O(1)

    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >=0:
        return rightRotation(rootNode)                 # ------------> TC = O(1)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)                  # ------------> TC = O(1)
    
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)                 # ------------> TC = O(1)
    
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = leftRotation(rootNode.rightChild)
        return leftRotation(rootNode)                  # ------------> TC = O(1)
    
    return rootNode

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "AVL Tree Deleted."

# newAVL = AVLNode(70)                        # ------------> TC = O(1), SC = O(1)
# newAVL = insertNode(newAVL, 90)
# newAVL = insertNode(newAVL, 50)
# newAVL = insertNode(newAVL, 100)
# newAVL = insertNode(newAVL, 80)
# newAVL = insertNode(newAVL, 60)
# newAVL = insertNode(newAVL, 30)
# newAVL = insertNode(newAVL, 20)
# newAVL = insertNode(newAVL, 40)
# levelOrder(newAVL)

# newAVL = AVLNode(5)
# newAVL = insertNode(newAVL, 10)
# newAVL = insertNode(newAVL, 15)
# newAVL = insertNode(newAVL, 20)
# newAVL = deleteNode(newAVL, 15)
# levelOrder(newAVL)

newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
deleteAVL(newAVL)
levelOrder(newAVL)