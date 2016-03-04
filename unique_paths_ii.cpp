# unique paths ii

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == None:
            return 0
        if len(obstacleGrid) == 0:
        	return 0
        else:
        	row_size = len(obstacleGrid)
        	col_size = len(obstacleGrid[0])
        	if obstacleGrid[0][0] == 1:
        	    return 0
        	else:
        	    obstacleGrid[0][0] = 1
        	i = 1
        	while i < row_size:
        		if obstacleGrid[i][0] == 1:
        			obstacleGrid[i][0] = 0
        			i = i + 1
        			while i < row_size:
        				obstacleGrid[i][0] = 0
        				i = i + 1
        			break
        		else:
        			obstacleGrid[i][0] = 1
        			i = i + 1
        	j = 1
        	while j < col_size:
        		if obstacleGrid[0][j] == 1:
        			obstacleGrid[0][j] = 0
        			j = j + 1
        			while j < col_size:
        				obstacleGrid[0][j] = 0
        				j = j + 1
        			break
        		else:
        			obstacleGrid[0][j] = 1
        			j = j + 1
        	for i in range(1, row_size):
        		for j in range(1, col_size):
        			if obstacleGrid[i][j] == 1:
        				obstacleGrid[i][j] = 0
        			else:
        				obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        	print obstacleGrid
        	return obstacleGrid[row_size - 1][col_size - 1]