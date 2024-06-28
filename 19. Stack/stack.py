# Stack creation

# Stack using List
#   Easy to implement
#   Speed problem when it grows

# Stack using Linked List
#   Fast performance
#   Implementation is not easy

class Stack:
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def __init__(self):
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

    # ! Push
    # Time Compexity : O(1)
    # Space Complexity: O(1)
    def push(self, value):
        self.list.append(value)
        return "The element is added."

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

stackc = Stack()
stackc.push(1)
stackc.push(2)
stackc.push(3)
# print(stackc.isEmpty())
# print(stackc)
stackc.pop()
# print(stackc)
# print(stackc.peek())
# stackc.delete()
# print(stackc)