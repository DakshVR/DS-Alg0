from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            for value in values:
                self.add(value)
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_value, max_value))
        return self
    
    def nthToLast(self, n):
        pointer1 = self.head
        pointer2 = self.head
        for i in range(n):
            if pointer1 is None:
                return None
            pointer1 = pointer1.next
        
        while pointer1:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer2


customLL = LinkedList()
customLL.generate(15, 0, 99)
print(customLL)
print(customLL.nthToLast(3))