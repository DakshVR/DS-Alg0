
# ! Heap Sort
# Step 1: insert data to binary heap tree
# Step 2: Extract data from binary heap
# It is best suited with array, it does not work with Linked List

#? Binary Heap: It is a binary tree with special properties
# The value of any given node must be less or equal of its children(min heap)
# The value of any given node must be greater or equal of its children(max heap)

def heapify(customList, n, i):                         #! TC: O(NLogN), SC: O(1)
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)

def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
    
    for i in range(n-1, 0, -1):
        customList[i] , customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    
    return customList.reverse()
    
my_list = [3, 5, 0, 6, 2, 1, 4]
print(heapSort(my_list))
