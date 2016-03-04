# spiral matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def printMatrixInCircle(matrix, start, col_size, row_size, result):
        	endX = col_size - 1 - start
        	endY = row_size - 1 - start
        	for i in range(start, endX + 1):
        		result.append(matrix[start][i])
        	if start < endY:
        		for i in range(start + 1, endY + 1):
        			result.append(matrix[i][endX])
        	if start < endX and start < endY:
        		r = range(start, endX)
        		rev_r = r[::-1]
        		for i in rev_r:
        			result.append(matrix[endY][i])
        	if start < endX and start < endY - 1:
        		r = range(start + 1, endY)
        		rev_r = r[::-1]
        		for i in rev_r:
        			result.append(matrix[i][start])

        if len(matrix) == 0:
        	return []
        row_size = len(matrix)
        col_size = len(matrix[0])
        start = 0
        result = []
        while row_size > start * 2 and col_size > start * 2:
        	printMatrixInCircle(matrix, start, col_size, row_size, result)
        	start = start + 1
        return result
