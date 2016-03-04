# 228. Summary Ranges My Submissions Question

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        beg = 0
        end = beg
        size = len(nums)
        ret = []
        while end < size:
            while end + 1 < size and nums[end + 1] - nums[end] == 1:
                end += 1
            if beg == end:
                ret.append(str(nums[beg]))
            else:
                ret.append(str(nums[beg]) + "->" + str(nums[end]))
            beg = end + 1
            end = beg
        return ret
                    
            
                    