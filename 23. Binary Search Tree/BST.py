
#! What is BST?

# Left Subtree the value of node is less than or equal to its parent node value.
# Right Subtree the value of the node is greater than its parent nodes value.

# Why need BST?

# Insertion and Deletion is Faster then Binary tree.

import queue 

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBST = BSTNode(None)                      # ------------> TC = O(1), SC = O(1)

print(newBST.data)
print(newBST.leftChild)

def insertNode(rootNode, nodeValue): #! ------------> TC = O(logN), SC = O(logN)
    if not rootNode.data:                              # ------------> TC = O(1)
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:                   # ------------> TC = O(1)
        if rootNode.leftChild is None:                 # ------------> TC = O(1)
            rootNode.leftChild = BSTNode(nodeValue)  
        else:
            insertNode(rootNode.leftChild, nodeValue) # -----------> TC = O(n/2)
    else:
        if rootNode.rightChild is None:                # ------------> TC = O(1)
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue) # ----------> TC = O(n/2)
    return "Successfull"

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# * Traversal

# * Depth First Search

# Preorder traversal
# --> Root Node
# --> Left Node
# --> Right Node
def preOrder(rootNode):                    #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return 
    print(rootNode.data)                               # ------------> TC = O(1)
    preOrder(rootNode.leftChild)                     # ------------> TC = O(n/2)
    preOrder(rootNode.rightChild)                    # ------------> TC = O(n/2)

print('\n')
print("This is Pre-Oder Traversal:" + '\n')
preOrder(newBST)

# Inorder traversal
# --> Left Node
# --> Root Node
# --> Right Node
def inOrder(rootNode):                     #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return 
    inOrder(rootNode.leftChild)                      # ------------> TC = O(n/2)
    print(rootNode.data)                               # ------------> TC = O(1)
    inOrder(rootNode.rightChild)                     # ------------> TC = O(n/2)

print('\n')
print("This is In-Oder Traversal:" + '\n')
inOrder(newBST)

# Postorder traversal
# --> Left Node
# --> Right Node
# --> Root Node
def postOrder(rootNode):                   #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return 
    postOrder(rootNode.leftChild)                    # ------------> TC = O(n/2)
    postOrder(rootNode.rightChild)                   # ------------> TC = O(n/2)
    print(rootNode.data)                               # ------------> TC = O(1)

print('\n')
print("This is Post-Oder Traversal:" + '\n')
postOrder(newBST)

# * Breadth First Search

# Level order traversal
# --> Level 1's Node Left Node and Right
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

print('\n')
print("This is Level-Oder Traversal:" + '\n')
levelOrder(newBST)


def searchNode(rootNode, nodeValue): #! ------------> TC = O(logN), SC = O(logN)
    if rootNode is None or rootNode.data is None:
        return "Node not found"
    if rootNode.data == nodeValue:                     # ------------> TC = O(1)
        return "Node Is Found"
    elif nodeValue < rootNode.data:                    # ------------> TC = O(1)
        if rootNode.leftChild is not None and rootNode.leftChild.data == nodeValue:                                     # ------------> TC = O(1)
            return "Found on Left"
        else:
            return searchNode(rootNode.leftChild, nodeValue) # -----------> TC = O(n/2)
    else:
        if rootNode.rightChild is not None and rootNode.rightChild.data == nodeValue:                                     # ------------> TC = O(1)
            return "Found on Right"
        else:
            return searchNode(rootNode.rightChild, nodeValue)# ----------> TC = O(n/2)

print('\n')
print("Searching for Node" + '\n')
print(searchNode(newBST, 100))


# To find Successor
def mimvalue(bstNode):
    currentNode = bstNode
    while (currentNode.leftChild is not None):
        currentNode = currentNode.leftChild
    return currentNode

def deleteNode(rootNode, nodeValue): #! ------------> TC = O(logN), SC = O(logN)
    if rootNode is None:            
        return rootNode                                # ------------> TC = O(1)
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)# ------------> TC = O(n/2)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)# ------------> TC = O(n/2)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild      # ------------> TC = O(1)
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild       # ------------> TC = O(1)
            rootNode = None
            return temp

        temp = mimvalue(rootNode.rightChild)  # ------------> TC = O(logN)
        rootNode.data = temp.data             # ------------> TC = O(1)
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # ------------> TC = O(n/2)
    return rootNode

print('\n')
print("Deletion for Node")
deleteNode(newBST, 20)
levelOrder(newBST)

def deleteBST(rootNode):                   #! ------------> TC = O(1), SC = O(1)
    rootNode.data = None                               # ------------> TC = O(1)
    rootNode.leftChild = None                          # ------------> TC = O(1)
    rootNode.rightChild = None                         # ------------> TC = O(1)
    return "The BST is Deleted"

print('\n')
print("Deletion for tree")
print(deleteBST(newBST))