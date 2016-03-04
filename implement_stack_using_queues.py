# Implement Stack using Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.queue2) != 0:
            self.queue2.append(x)
        else:
            self.queue1.append(x)
        
    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.queue1) != 0:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            del self.queue1[0]
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            del self.queue2[0]

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue1) != 0:
            return self.queue1[-1]
        else:
            return self.queue2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return True
        else:
            return False