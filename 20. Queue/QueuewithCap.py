class Queue:
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isFull(self):
        if self.start + 1 == self.start:
            return True
        elif self.start == 0 and self.top == self.maxSize:
            return True
        else:
            return False
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def enqueue(self, value):
        if self.isFull():
            return "The queue is Full"
        else:
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "Added the value"

customQ = Queue(3)
print(customQ.isFull())
print(customQ.isEmpty())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
customQ.enqueue(3)
print(customQ)
print(customQ.isFull())