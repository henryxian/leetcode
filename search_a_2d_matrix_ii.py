# Search a 2D Matrix II
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix):
            return False
            
        dim_row = len(matrix)
        dim_col = len(matrix[0])
        m = 0
        n = dim_col - 1
        while m >= 0 and m <= dim_row - 1 and n >= 0 and n <= dim_col - 1:
            if target == matrix[m][n]:
                return True
            elif target > matrix[m][n]:   
                m = m + 1	# TODO: 这一步可以用二分查找
            else:
                n = n - 1
        return False
        
