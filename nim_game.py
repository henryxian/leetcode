# Nim Game
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        else:
            if self.canWinNim(n - 1) and self.canWinNim(n - 2) and self.canWinNim(n - 3):
                return False
            else:
                return True

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
        	return True
        n1 = True
        n2 = True
        n3 = True
        n = n - 3
        while n:
        	n4 = not (n1 and n2 and n3)
        	n1 = n2
        	n2 = n3
        	n3 = n4
        	n = n - 1
        return n4

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 != 0:
            return True
        else:
            return False       
