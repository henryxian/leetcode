# Power of Three
# class Solution(object):
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n <= 0:
#         	return False
#         else:
#         	n = str(n)
#         	sum = 0
#         	for i in n:
#         		i = int(i)
#         		sum = sum + i
#         	if sum % 3 == 0:
#         		return True
#         	else:
#         		return False

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
        	return False
        return (True if 1162261467 % n == 0 else False)

if __name__ == '__main__':
	solution = Solution()
	# False
	print solution.isPowerOfThree(0)
	# True
	print solution.isPowerOfThree(3)
	# True
	print solution.isPowerOfThree(9)
	# True
	print solution.isPowerOfThree(81)
	# False
	print solution.isPowerOfThree(2)
	# False
	print solution.isPowerOfThree(4)
	# False
	print solution.isPowerOfThree(-1)
	# False
	print solution.isPowerOfThree(45)

