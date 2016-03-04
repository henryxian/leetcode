# Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        prev = nums[0]
        for n in nums:
            if n == prev:
                cnt = cnt + 1
            else:
                cnt = cnt - 1
            if cnt == 0:
                prev = n
                cnt = cnt + 1
        return prev