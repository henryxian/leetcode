# Pascal's Triangle II
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def combination(k, n):
            return factorial(n) / ( factorial(k) * factorial(n - k))
            
        def factorial(n):
            result = 1
            while n:
                result = n * result
                n = n - 1
            return result
           
        if rowIndex < 0:
            return []
        rowIndex = rowIndex + 1
        kth_row = []
        count = 1
        while count <= rowIndex:
            kth_row.append(combination(count - 1, rowIndex - 1))
            count = count + 1
        return kth_row