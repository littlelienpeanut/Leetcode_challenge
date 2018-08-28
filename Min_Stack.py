class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float('inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.min_val = min(self.min_val, x)
        
    def pop(self):
        """
        :rtype: void
        """
        
        self.stack = self.stack[:-1]
        if len(self.stack) == 0:
            self.min_val = float('inf')
        else:
            self.min_val = min(self.stack)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
