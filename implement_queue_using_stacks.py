# Implement Queue using Stacks
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack2) != 0:
            self.stack2.pop()
        else:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            self.stack1.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        len1 = len(self.stack1)
        if len1 != 0:
            return self.stack1[0]
        len2 = len(self.stack2)
        if len2 != 0:
            return self.stack2[len2 - 1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False
        