# Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
        	return False
        if n == 1:
        	return True
        while n > 1:
        	if n % 2 == 0:
        		n = n >> 1
        	else:
        		return False
        return True
        
if __name__ == '__main__':
	solution = Solution()
	# False
	print solution.isPowerOfTwo(-1)
	# False
	print solution.isPowerOfTwo(0)
	# False
	print solution.isPowerOfTwo(3)
	# False
	print solution.isPowerOfTwo(6)
	# True
	print solution.isPowerOfTwo(2)
	# True
	print solution.isPowerOfTwo(128)
	# 