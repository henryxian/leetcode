# 172. Factorial Trailing Zeroes

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            sum = sum + n / 5
            n = n / 5
        return sum