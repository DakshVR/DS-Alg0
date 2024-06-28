class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Stack:
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            nodeval = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            return nodeval
    
    def peep(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            nodeval = self.LinkedList.head.value
            return nodeval
    
    # ! delete
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def delete(self):
        self.LinkedList.head = None
    
customStack = Stack()
customStack.push(1)
customStack.push(2)
print(customStack.isEmpty())
print(customStack)
print(customStack.pop())
print(customStack)