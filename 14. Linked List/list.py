#  It is a form of a sequential collection and it does not have to be in order. A linked list is made up of independent nodes that may contain any type of data and each node has a referenece to the next node in the link.

# * NOdes: Data And Reference

# * Types of Linked List
# Singly Linked List
# circular Linked List
# doubly Linked List
# circular doubly Linked List

# *! Node Class

# Time COmplexity: O(1)
# Space complexity: O(1)

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# newNode = Node(10)
# print(newNode)   # Prints the address of the node.
# print(newNode.value)    #prints actual value of the node

# *! Linked list Class

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# Time COmplexity: O(1)
# Space complexity: O(1)
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# newNode = LinkedList(10)
# print(newNode.head.value)


# *! Insertion to Linked List

# We can add to beginning, middle and end of linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # ! Insertion
    # Time COmplexity: O(1)
    # Space complexity: O(1)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    # ! Prepend, add to begining of the list
    # Time COmplexity: O(1)
    # Space complexity: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    # ! Insert, add at any index
    # Time COmplexity: O(n)
    # Space complexity: O(1)
    def insert(self, value, index):
        new_node = Node(value)
        temp_node = self.head
        if index <0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
    
    # ! Traverse
    # Time COmplexity: O(n)
    # Space complexity: O(1)
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    # ! Search
    # Time COmplexity: O(n)
    # Space complexity: O(1)
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    # ! Get
    # Time COmplexity: O(n)
    # Space complexity: O(1)
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < 0 or index >= self.length:
            return False
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
    
    # ! Set
    # Time COmplexity: O(n)
    # Space complexity: O(1)
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # ! Pop First
    # Time COmplexity: O(1)
    # Space complexity: O(1)
    def pop_first(self):
        pop_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head == None
            self.tail == None
        else:
            self.head = self.head.next
            pop_node.next = None
        self.length -=1
        return pop_node
    
    # ! Pop 
    # Time COmplexity: O(N)
    # Space complexity: O(1)
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            pop_node = self.tail
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.length -=1
            return pop_node.value
        
    # ! Remove 
    # Time COmplexity: O(N)
    # Space complexity: O(1)
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        pop_node = prev_node.next
        prev_node.next = pop_node.next
        pop_node.next = None
        self.length -=1
        return pop_node

    # ! Delete All 
    # Time COmplexity: O(1)
    # Space complexity: O(1)
    def delet_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_list = LinkedList()
new_list.prepend(10)
new_list.append(20)
new_list.append(30)
print(new_list.length)
# new_list.append(40)
# new_list.prepend(100)
# new_list.insert(55, 3)
# print(new_list)
# new_list.traverse()
# print(new_list.search(400))
# print(new_list.get(5))
# print(new_list.set(1, 333))
print(new_list)
# print(new_list.pop_first())
# print(new_list)
# print(new_list.pop())
# print(new_list)
# print(new_list.remove(2))
# print(new_list)
print(new_list.delet_all())
print(new_list)