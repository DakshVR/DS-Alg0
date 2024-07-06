
#? What is a Binary Heap
#* A Binary Heap is a Bunary Tree with the followinf properties.

# --> A Binary heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among the keys present in Binary Heap. The same property must be recursivey true for all the nodes in Binary Tree.
# --> Its a oomplete tree (All levels are completely filled except possibly the last level and the least level has all the keys as lest as possible). This property of Binary Heap makes them suitable to be stored in an array.

#? Common Operations
#* Creation of Binary Heap
#* Peek top of Binary Heap
#* Extract Min/ Extract Max
#* Traversal of Binary Heap
#* Size of Binary Heap
#* Insert value in Binary Heap
#* Delete entire Binary Heap

#? Implementation Options
#* Array Implementation   ---> Best Fit for Binary Heap
#* Reference/pointer Implementation

#? How is it stored?

#*   0    1     2     3     4     5     6    7     8
#* | x || 5 || 10 || 20 || 30 || 40 || 50 || 60 ||   |

#* Left child = cell[2x]
#* Right child = cell[2x + 1]
#* Leave index 0, as it becomes easy to calculate the indexes of the remaining elements

#! Creation of Binary Heap
#* Initialize fixed size List
#* set size of the Binary Heap to 0, as no elements are present 

class Heap():
    def __init__(self, size):                   
        self.customList = (size+1) * [None]            # ------------> TC = O(1)
        self.heapsize = 0                              # ------------> TC = O(1)
        self.maxsize = size + 1   # +1 becuase we won't use index 0


newBinaryHeap = Heap(5)                    #! ------------> TC = O(1), SC = O(n)


#! Peek top of Binary Heap
#* We return the root.
#* Return List[1]

def peekofHeap(rootNode):                  #! ------------> TC = O(1), SC = O(1)
    if not rootNode:                                   # ------------> TC = O(1)
        return
    return rootNode.customList[1]                      # ------------> TC = O(1)


#! Size of Binary Heap
#* Return of Filled cells

def sizeOfheap(rootNode):                  #! ------------> TC = O(1), SC = O(1)
    if not rootNode:                                   # ------------> TC = O(1)
        return 0                                       # ------------> TC = O(1)
    else:
        return rootNode.heapsize                       # ------------> TC = O(1)

# print(sizeOfheap(newBinaryHeap))


#! Traversal of Binary Heap
#* We again have 4 traversal as Binary Search Tree or Binary tree.
#* Level Order

def levelOrder(rootNode):                  #! ------------> TC = O(n), SC = O(1)
    if not rootNode:                                   # ------------> TC = O(1)
        return
    else:
        for i in range(1, rootNode.heapsize+1):        # ------------> TC = O(n)
            print(rootNode.customList[i])              # ------------> TC = O(1)


#! Insert value in Binary Heap
#* Find unused cell and insert the value
#* Check it the parents value is greater, if so swap until the root is the smallest value. We need to maintain the property
            
def heapifyTreeInsert(rootNode, index, heapType): #! ------------> TC = O(LogN), SC = O(LogN)
    parentIndex = int(index / 2)                       # ------------> TC = O(1)
    if index <= 1:                                     # ------------> TC = O(1)
        return
    if heapType == "Minimum":                          # ------------> TC = O(1)
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)# ------------> TC = O(LogN) 
    elif heapType == "Maximum":                        # ------------> TC = O(1)
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType) # ------------> TC = O(LogN)

def insertNode(rootNode, nodeValue, heapType):#! ------------> TC = O(LogN), SC = O(LogN)
    if rootNode.heapsize + 1 == rootNode.maxsize:      # ------------> TC = O(1)
        return "The Binary heap is full."              # ------------> TC = O(1)
    rootNode.customList[rootNode.heapsize + 1] = nodeValue # ------------> TC = O(1)
    rootNode.heapsize += 1                             # ------------> TC = O(1)
    heapifyTreeInsert(rootNode, rootNode.heapsize, heapType) # ------------> TC = O(logN)
    return "Value is Inserted"

# newheap = Heap(5)
# insertNode(newheap, 4, "Minimum")
# insertNode(newheap, 5, "Minimum")
# insertNode(newheap, 2, "Minimum")
# insertNode(newheap, 1, "Minimum")
# levelOrder(newheap)

#! Extract Min/Extract Max
#* We can only Extract root, other extraction of element is not allowed as per the property of the Binary Heap.
#* Once root is extracted, we need to make adjustments.
#* For example, if it is Min heap, we replace it with last element, which is to be found on the very left on last level.
#* Then replace the root with the minimum children which is found on left and keep on swapping until the property of min heap is met.

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 +1
    swapChild = 0
    
    if rootNode.heapsize < leftIndex:
        return
    elif rootNode.heapsize == leftIndex:
        if heapType == "Minimum":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Minimum":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType): #! ------------> TC = O(LogN), SC = O(LogN)
    if rootNode.heapsize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapsize]
        rootNode.customList[rootNode.heapsize] = None
        rootNode.heapsize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractNode

#! Delete entire Binary Heap
#* CusttomList = [None] 
    
def deletHeap(rootNode):                   #! ------------> TC = O(1), SC = O(1)
    rootNode.customList = None

newheap = Heap(5)
insertNode(newheap, 4, "Maximum")
insertNode(newheap, 5, "Maximum")
insertNode(newheap, 2, "Maximum")
insertNode(newheap, 1, "Maximum")
extractNode(newheap)
levelOrder(newheap)

