# Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def max_sum(index):
            if index == 0:
                return nums[index]
            elif max_sum(index - 1) <= 0:
                return nums[index]
            else:
                return nums[index] + max_sum(index - 1)
        
        length = len(nums)
        max = max_sum(0)
        for i in range(length):
            sum = max_sum(i)
            max = sum if sum > max else max
        return max

# O(n) solution        
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        cur_sum = 0
        max = nums[0]
        for i in xrange(length):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum = cur_sum + nums[i]
            if cur_sum > max:
                max = cur_sum
        return max