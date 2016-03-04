# 198. House Robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        else:
            size = len(nums)
            rob_num = [0,] * size
            rob_num[0] = nums[0]
            rob_num[1] = max(nums[0], nums[1])
            for i in range(2, size):
                rob_num[i] = max(rob_num[i - 1], rob_num[i - 2] + nums[i])
            return rob_num[size - 1]
        