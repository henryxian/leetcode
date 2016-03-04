# 202. Happy Number

class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n <= 0:
			return False
		seq = []
		while n:
			sum = 0
			while n:
				remainder = n % 10
				sum = sum + remainder * remainder
				n = n / 10
			if sum == 1:
				return True
			elif sum not in seq:
				seq.append(sum)
				n = sum
			else:
				return False
if __name__ == '__main__':
	solution = Solution()
	print solution.isHappy(19)                