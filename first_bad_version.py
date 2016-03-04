# First Bad Version
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = len(n)
        low = 0
        badVersion = -1
        while mid > low:
        	mid = (high + low) / 2 
        	if isBadVersion(n[mid]):
        		high = mid - 1
        	else:
        		low = mid + 1


if __name__ == '__main__':
	solution = Solution()
	solution.firstBadVersion()
