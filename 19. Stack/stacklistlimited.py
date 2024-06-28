class Stack:
    #  Time Compexity : O(1)
    # Space Complexity: O(1)
    def __init__(self, maxSize) -> None:
        self.maxsize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # ! IS Empty
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # ! IS Full
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
    
    # ! Push
    # Time Compexity : O(1) / O(n^2)
    # Space Complexity: O(1)
    def push(self, value):
        if self.isFull():
            return "The Stack is FUll"
        else:
            self.list.append(value)
            return "Added the element"
    
    # ! Pop
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def pop(self):
        if self.isEmpty():
            return "Not any element in the Stack"
        else:
            return self.list.pop()
    
    # ! peek
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def peek(self):
        if self.isEmpty():
            return "Not any element in the Stack"
        else:
            return self.list[len(self.list)-1]
        
    # ! delete
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def delete(self):
        self.list = None

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(3)
print(customStack)
print(customStack.isFull())
