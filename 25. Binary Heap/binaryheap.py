
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

print(sizeOfheap(newBinaryHeap))


#! Traversal of Binary Heap
#* We again have 4 traversal as Binary Search Tree or Binary tree.
#* Level Order

def levelOrder(rootNode):                  #! ------------> TC = O(n), SC = O(1)
    if not rootNode:                                   # ------------> TC = O(1)
        return
    else:
        for i in range(1, rootNode.heapsize+1):        # ------------> TC = O(n)
            print(rootNode.customList[i])              # ------------> TC = O(1)