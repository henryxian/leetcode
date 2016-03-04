# Add Digits
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
        	return num
        else:
        	remainder = num % 9
        	if remainder:
        		return remainder
        	else:
        		return remainder + 9

if __name__ == '__main__':
 	solution = Solution()
 	# 2
 	print solution.addDigits(38)
 	# 1
 	print solution.addDigits(1)
 	# 2
 	print solution.addDigits(29)
 	# 9
 	print solution.addDigits(18)
 	# 9
 	print solution.addDigits(36)