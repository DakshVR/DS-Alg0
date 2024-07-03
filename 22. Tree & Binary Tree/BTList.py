class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):           #! ------------> TC = O(1), SC = O(1)
        if self.lastUsedIndex + 1 == self.maxSize:     # ------------> TC = O(1)
            return "This BT is Full."
        self.customList[self.lastUsedIndex+1] = value  # ------------> TC = O(1)
        self.lastUsedIndex += 1                        # ------------> TC = O(1)
        return "Value is Inserted"

    def searchNode(self, nodeValue):       #! ------------> TC = O(n), SC = O(1)
        for i in range(len(self.customList)):          # ------------> TC = O(n)
            if self.customList[i] == nodeValue:        # ------------> TC = O(1)
                return "Success"
        return "Node doesn't exist"
    
    def preOrder(self, index):             #! ------------> TC = O(n), SC = O(1)
        if index > self.lastUsedIndex:                 # ------------> TC = O(1)
            return
        print(self.customList[index])                  # ------------> TC = O(1)
        self.preOrder(2*index)                       # ------------> TC = O(n/2)
        self.preOrder(2*index + 1)                   # ------------> TC = O(n/2)

    def inOrder(self, index):              #! ------------> TC = O(n), SC = O(1)
        if index > self.lastUsedIndex:                 # ------------> TC = O(1)
            return
        self.inOrder(2*index)                        # ------------> TC = O(n/2)
        print(self.customList[index])                  # ------------> TC = O(1)
        self.inOrder(2*index + 1)                    # ------------> TC = O(n/2)

    def postOrder(self, index):            #! ------------> TC = O(n), SC = O(1)
        if index > self.lastUsedIndex:                 # ------------> TC = O(1)
            return
        self.postOrder(2*index)                      # ------------> TC = O(n/2)
        self.postOrder(2*index + 1)                  # ------------> TC = O(n/2)
        print(self.customList[index])                  # ------------> TC = O(1)

    def levelOrder(self, index):           #! ------------> TC = O(n), SC = O(1)
        for i in range(index, self.lastUsedIndex+1):   # ------------> TC = O(n)
            print(self.customList[i])                  # ------------> TC = O(1)

    def deleteNode(self, value):           #! ------------> TC = O(n), SC = O(1)
        if self.lastUsedIndex == 0:                    # ------------> TC = O(1)
            return "Nothing to Delete"
        for i in range(1, self.lastUsedIndex+1):       # ------------> TC = O(n)
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node is Deleted"
    
    def deleteBT(self):                    #! ------------> TC = O(1), SC = O(1)
        self.customList = None

newBT = BinaryTree(8)                      #! ------------> TC = O(1), SC = O(n)

print('\n')
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
print('\n')
print(newBT.searchNode("Tea"))

print('\n')
print("This is Pre-Oder Traversal:" + '\n')
newBT.preOrder(1)

print('\n')
print("This is In-Oder Traversal:" + '\n')
newBT.inOrder(1)

print('\n')
print("This is Post-Oder Traversal:" + '\n')
newBT.postOrder(1)

print('\n')
print("This is Level-Oder Traversal:" + '\n')
newBT.levelOrder(1)

newBT.deleteNode("Hot")

print('\n')
print("This is Level-Oder Traversal:" + '\n')
newBT.levelOrder(1)
