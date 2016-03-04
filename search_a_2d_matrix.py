# Search a 2D Matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for row in matrix:
        #     for i in row:
        #         if i == target:
        #             return True
        # return False

        # binary search
        row_dim = len(matrix)
        col_dim = len(matrix[0])
        length = row_dim * col_dim
        low = 0
        high = length - 1
        while low <= high :
        	mid = (low + high) / 2
        	idx = mid / col_dim
        	idy = mid % col_dim
        	print idx, idy
        	curr = matrix[idx][idy]
        	if curr == target:
        		return True
        	elif curr < target:
        		low = mid + 1
        	else:
        		high = mid - 1
        return False        