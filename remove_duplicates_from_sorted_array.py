# remove duplicates from sorted array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        if len(nums) == 1:
        	return 1
        else:
        	size = len(nums)
        	prev = nums[0]
        	count = 0
        	index = 1
        	while index < size:
        		if prev == nums[index]:
        			pass
        		else:
        			count = count + 1
        			nums[count] = nums[index]
        		prev = nums[index]
        		index = index + 1
        return count + 1