#! What is BST?

# Left Subtree the value of node is less than or equal to its parent node value.
# Right Subtree the value of the node is greater than its parent nodes value.

# Why need BST?

# Insertion and Deletion is Faster then Binary tree.


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


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
    

newBST = BSTNode(None)                      # ------------> TC = O(1), SC = O(1)

print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(newBST.data)
print(newBST.leftChild.data)