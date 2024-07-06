
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