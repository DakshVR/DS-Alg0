# Use a single python list to implement three stacks.

class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.customeList = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
    
    def isFull(self, stacksum):
        if self.sizes [stacksum]