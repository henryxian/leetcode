# Excel Sheet Column Title

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = ""
        while n != 0:
        	remainder = n % 26
        	n = n / 26

        	# 为26的整数倍，该位置设置为Z，n减1
        	if remainder == 0: 
        		# 当然，按照进制转换的方法（不断地除26取余数），
        		# 不可能有26的余数，比如：52->(20)->AZ，
        		# 此时余数是0，这种情况要特殊处理，
        		# 很简单，如下面的代码所示：
        		n = n - 1
        		result = "Z" + result
        	else:
        		result = chr(remainder + 64) + result
        return result
if __name__ == '__main__':
	solution = Solution()
	print solution.convertToTitle(1)
	print solution.convertToTitle(2)
	print solution.convertToTitle(3)
	print solution.convertToTitle(26)
	print solution.convertToTitle(27)
	print solution.convertToTitle(28)
	print solution.convertToTitle(52)
