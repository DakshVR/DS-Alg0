class Queue:
    # Space Complexity : O(1)
    # Time  Complexity : O(1)
    def __init__(self):
        self.items = []
    
    def __str__(self):
        value = [str(x) for x in self.items]
        return ' '.join(value)

    # Space Complexity : O(1)
    # Time  Complexity : O(1)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    # Space Complexity : O(1)
    # Time  Complexity : O(n), worst case O(n^2)
    def enqueue(self, value):
        self.items.append(value)
        return "Element is Insert at the end of the list."
    
    # Space Complexity : O(1)
    # Time  Complexity : O(n)
    def dequeue(self):
        if self.isEmpty():
            return "Nothing to Dequeue"
        else:
            return self.items.pop(0)
    
    # Space Complexity : O(1)
    # Time  Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Nothing to Dequeue"
        else:
            return self.items[0]
    
    # Space Complexity : O(1)
    # Time  Complexity : O(1)
    def delete(self):
        self.items = None

customQ = Queue()
# print(customQ.isEmpty())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
customQ.enqueue(4)
print(customQ)
customQ.dequeue()
print(customQ)
print(customQ.peek())
customQ.delete()
