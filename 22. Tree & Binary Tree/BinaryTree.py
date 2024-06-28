import QueuewithCap
import queue 

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None 

newBT = TreeNode("Drinks") # ------------> TC = O(1), SC = O(1)
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
# soda = TreeNode("Soda")
# beer = TreeNode("Beer")
# rightChild.leftChild = soda
# rightChild.rightChild = beer
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrder(rootNode):             #! ------------> TC = O(n), SC = O(n) : becuase we are using Stack memory, due to recursive method.
    if not rootNode:                # ------------> TC = O(1)
        return              
    print(rootNode.data)            # ------------> TC = O(1)
    preOrder(rootNode.leftChild)    # ------------> TC = O(n/2)
    preOrder(rootNode.rightChild)   # ------------> TC = O(n/2)

print('\n')
print("This is Pre-Oder Traversal:" + '\n')
preOrder(newBT)

def inOrder(rootNode):              #! ------------> TC = O(n), SC = O(n)
    if not rootNode:                # ------------> TC = O(1)
        return
    inOrder(rootNode.leftChild)     # ------------> TC = O(n/2)
    print(rootNode.data)            # ------------> TC = O(1)
    inOrder(rootNode.rightChild)    # ------------> TC = O(n/2)

print('\n')
print("This is In-Oder Traversal:" + '\n')
inOrder(newBT)

def postOrder(rootNode):            #! ------------> TC = O(n), SC = O(n)
    if not rootNode:                # ------------> TC = O(1)
        return
    postOrder(rootNode.leftChild)   # ------------> TC = O(n/2)
    postOrder(rootNode.rightChild)  # ------------> TC = O(n/2)
    print(rootNode.data)            # ------------> TC = O(1)

print('\n')
print("This is Post-Oder Traversal:" + '\n')
postOrder(newBT)

# # ? HINT: USE Queue
def levelOrder(rootNode):              #! ------------> TC = O(n), SC = O(n)
        if not rootNode:
            return "res"
        else:
            CustomeQueue = queue.Queue()
            CustomeQueue.put(rootNode)
            while not (CustomeQueue.empty()):
                root = CustomeQueue.get()
                print(root.data)
                if (root.leftChild is not None):
                    CustomeQueue.put(root.leftChild)
                if (root.rightChild is not None):
                    CustomeQueue.put(root.rightChild)

print('\n')
print("This is Level-Oder Traversal:" + '\n')
levelOrder(newBT)


# 
def searchBT(rootNode, nodeValue):        #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return 0
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not (customQueue.empty()):
            root = customQueue.get()
            if root.data == nodeValue:
                return "Search BT Success"
            if (root.leftChild is not None):
                customQueue.put(root.leftChild)
            if (root.rightChild is not None):
                customQueue.put(root.rightChild)
        return "Not Found"
    
print('\n')
print(searchBT(newBT, "Tea"))


def insertBT(rootNode, newNode):         #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        rootNode =  newNode
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not (customQueue.empty()):
            root = customQueue.get()
            if (root.leftChild is not None):
                customQueue.put(root.leftChild)
            else:
                root.leftChild = newNode
                return "Success inserting on left"
            if (root.rightChild is not None):
                customQueue.put(root.rightChild)
            else:
                root.rightChild = newNode
                return "Success inserting on right"
            
soda = TreeNode("Soda")
print(insertBT(newBT, soda))
beer = TreeNode("Beer")
print(insertBT(newBT, beer))

print('\n')
print("This is Level-Oder Traversal:" + '\n')
levelOrder(newBT)

# ! Delete Node

def getDeepestNode(rootNode):  #! ------------> TC = O(n), SC = O(n)
    if not rootNode:
        return 
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not customQueue.empty():
            root = customQueue.get()
            if root.leftChild is not None:
                customQueue.put(root.leftChild)
            if root.rightChild is not None:
                customQueue.put(root.rightChild)
        return root  # Return the deepest node itself


def deleteDeepestNode(rootNode, deepestNode):#! ------------> TC =O(n),SC = O(n)
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not customQueue.empty():
            root = customQueue.get()
            if root is deepestNode:
                root.data = None
                return
            if root.rightChild:
                if root.rightChild is deepestNode:
                    root.rightChild = None
                    return
                else:
                    customQueue.put(root.rightChild)
            if root.leftChild:
                if root.leftChild is deepestNode:
                    root.leftChild = None
                    return
                else:
                    customQueue.put(root.leftChild)

def deleteNodeBT(rootNode, node):            #! ------------> TC =O(n),SC = O(n)
    if not rootNode:
        return "NO BT"
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not(customQueue.empty()):
            root = customQueue.get()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node is successfullt deleted"
            if (root.leftChild is not None):
                    customQueue.put(root.leftChild)
            if (root.rightChild is not None):
                    customQueue.put(root.rightChild)
        return "Failed to delete"

print('\n')
print(deleteNodeBT(newBT, 'Tea'))
levelOrder(newBT)

def deleteBT(rootNode):                 #! ------------> TC =O(1),SC = O(1)
    rootNode.data = None                # ------------> TC = O(1)
    rootNode.leftChild = None           # ------------> TC = O(1)
    rootNode.rightChild = None          # ------------> TC = O(1)
    return "TREE IS DELETED"            # ------------> TC = O(1)

print(deleteBT(newBT))