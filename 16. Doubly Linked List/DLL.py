class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
          
    #! Creation of Doubly linked list
    # Time Complexity = O(1)
    # Space Complexity = O(1)
    def createDLL(self, nodevalue):
        node = Node(nodevalue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "Created Successfully"
    
    #! Insertion of Doubly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def insert(self, nodevalue, index):
        # insert at beginning 
        if self.head is None:
            return "Cannot be Inserted"
        else:
            newnode = Node(nodevalue)
            if index == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif index == 1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                counter = 0
                while counter < index -1:
                    tempnode = tempnode.next
                    counter +=1
                nextnode = tempnode.next
                newnode.next = nextnode
                nextnode.prev = newnode
                tempnode.next = newnode
                newnode.prev = tempnode

        # insert at the end
        # insert at the last
        pass

    #! Traverse of Doubly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    
    #! ReverseTraverse of Doubly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def reversetraverse(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev
      
    
    #! Search of Doubly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return f'Node with value {value} exists.'
            node = node.next
        return (f'Node with value {value} is not present')
            
    
    #! Deletion of element Doubly linked list
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def delete(self, location):
        if self.head is None:
            return "Nothing To Delete."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # popnode = self.head
                    # newhead = popnode.next
                    # newhead.prev = None
                    # self.head = newhead
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index +=1
                popnode = tempnode.next
                nextnode = popnode.next
                nextnode.prev = tempnode
                tempnode.next = nextnode

    #! Clear all element Doubly linked list
    # Time Complexity = O(1)
    # Space Complexity = O(1)
    def clear(self):
        self.head = None
        self.tail = None


DLL= DoublyLinkedList()
DLL.createDLL(3)
DLL.insert(5,0)
DLL.insert(0,1)
DLL.insert(4,2)
DLL.insert(55,2)
# DLL.traverse()
# DLL.reversetraverse()
# print(DLL.search(545))
# DLL.delete(2)
# DLL.delete(2)
# DLL.delete(1)
# DLL.delete(0)
# DLL.delete(0)
# DLL.delete(0)
DLL.clear()
print([node.value for node in DLL])