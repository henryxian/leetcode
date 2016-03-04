# Pascal's Triangle
class Solution(object):
        
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def combination(k, n):
            return factorial(n) / ( factorial(k) * factorial(n - k))
            
        def factorial(n):
            result = 1
            while n:
                result = n * result
                n = n - 1
            return result    
        
        if numRows == 0:
            return []
        upper_index = numRows + 1
        pascal = []
        for nth_row in xrange(1, upper_index):
            line = []
            index = 1
            while index <= nth_row:
                line.append(combination(index - 1, nth_row - 1))
                index = index + 1
            pascal.append(line)
        return pascal