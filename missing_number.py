# 268. Missing Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        n = len(nums)
        for i in range(1, n + 1):
            xor ^= i
        for i in nums:
            xor ^= i
        return xor