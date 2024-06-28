class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
 
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
          

    #! Creation of Circular singly linked list
    # Time Complexity = O(1)
    # Space Complexity = O(1)
    def createCSLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "Created"
    
    #! Insertion of Circular singly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def insert(self, nodevalue, index):
        if self.head is None:
            return 'The head is None'
        else:
            newnode = Node(nodevalue)
            if index == 0:
                newnode.next = self.head
                self.head = newnode
                self.tail.next = newnode
            elif index == 1:
                newnode.next = self.tail.next
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                for _ in range(index-1):
                    tempnode = tempnode.next
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
            return "Successful"

    #! Traverse of Circular singly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def traverse(self):
        node = self.head
        while node.next is not None:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break
    
    #! Search of Circular singly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def search(self, value):
        node = self.head
        while node.next is not None:
            if node.value == value:
                return node.value
            node = node.next
            if node == self.tail.next:
                return "Not found"
    
    #! Deletion of element Circular singly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def delete(self, index):
        if self.head == None:
            return "No nodes Found"
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif index == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < index-1:
                    node = node.next
                    index +=1
                nextnode = node.next
                node.next = nextnode.next

    #! Clear of element Circular singly linked list
    # Time Complexity = O(1)
    # Space Complexity = O(1)
    def clear(self):
        self.head = None
        self.tail.next = None
        self.tail = None


CSL= CircularSinglyLinkedList()
CSL.createCSLL(1)
CSL.insert(2,0)
CSL.insert(3,1)
CSL.insert(4,2)
# CSL.traverse()
# print(CSL.search(43))

print([node.value for node in CSL])
CSL.delete(1)
print([node.value for node in CSL])

CSL.clear()
print([node.value for node in CSL])