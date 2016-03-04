# Min Stack
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stack) == 0:
        	self.min_stack.append(x)
        else:
            length = len(self.min_stack)
            min_top = self.min_stack[length - 1]
            if x >= min_top:
                self.min_stack.append(min_top)
            else:
                self.min_stack.append(x)
        self.stack.append(x)
                
    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        length = len(self.stack)
        return self.stack[length - 1]
        
    def getMin(self):
        """
        :rtype: int
        """
        length = len(self.min_stack)
        return self.min_stack[length - 1]