# Wiggle Sort II
# 怎样证明方法的正确性和合理性？
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        s, t = (len(nums) + 1) >> 1, len(nums)
        for i in xrange(len(nums)):
            if i & 1 == 0:
                s -= 1
                nums[i] = temp[s]
            else:
                t -= 1
                nums[i] = temp[t]
        print nums