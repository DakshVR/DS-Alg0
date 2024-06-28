class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL:
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
    
    # ! Creation of Circular Doubly Linked List
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
    
    # ! Insertion of Circular Doubly Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def insert(self, location, value):
        newnode = Node(value)
        if self.head is None:
            return
        else:
            if location == 0:
                    newnode.next = self.head
                    newnode.prev = self.tail
                    self.head.prev = newnode
                    self.head = newnode
                    self.tail.next = newnode
            elif location == 1:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.tail.next = newnode
                self.tail= newnode
            else:
                index = 0
                tempnode = self.head
                while index < location-1:
                    tempnode = tempnode.next
                    index +=1
                newnode.next = tempnode.next
                tempnode.next.prev = newnode
                tempnode.next = newnode
                newnode.prev = tempnode
                
    # ! Insertion of Circular Doubly Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def traverse(self):
        if self.head is None:
            print("Nothign to Traverse")
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next
    
    # ! Reverse of Circular Doubly Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head is None:
            print("Nothign to Traverse")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev
    
    # ! Search of Circular Doubly Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head is None:
            print("Nothign to Traverse")
        else:
            node = self.head
            while node:
                if node.value == value:
                    return (f'node with value {value} Exist')
                if node == self.tail:
                    return 'Node with Vlaue does not exist'
                node = node.next
    
    # ! Deletion of Circular Doubly Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, location):
        if self.head is None:
            print('Nothing')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    # newhead = self.head.next
                    # newhead.prev = self.head.prev
                    # self.head = newhead
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                node = self.head
                index = 0
                while index < location-1:
                    node = node.next
                    index +=1
                popnode = node.next
                nextnode = popnode.next
                node.next = nextnode
                nextnode.prev = node
        
    # ! Clear of Circular Doubly Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def clear(self):
        # self.head.next = None
        # self.head.prev = None
        # self.head = None
        # self.tail = None
        if self.head is None:
            print('Nothing to Delete')
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None

DCSL = CircularDLL()
DCSL.create(3)
DCSL.insert(0,0)
DCSL.insert(1,1)
DCSL.insert(2,4)
# DCSL.insert(2,44)
# DCSL.insert(3,434)
# DCSL.traverse()
# DCSL.reverse()
# print(DCSL.search(41))

print([node.value for node in DCSL])
DCSL.clear()
print([node.value for node in DCSL])