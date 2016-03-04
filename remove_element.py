# Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        index_not_val = 0
        count = 0
        while(index < length):
        	if (nums[index] != val):
        		count = count + 1
        	index = index + 1

        index = 0
        while (index_not_val < length):
        	if nums[index_not_val] != val:
        		nums[index] = nums[index_not_val]
        		index = index + 1
        		index_not_val = index_not_val + 1
        	else:
        		while index_not_val < length and nums[index_not_val] == val:
        			index_not_val = index_not_val + 1

        del nums[count:]
        return count

if __name__ == '__main__':
	solution = Solution()
	li1 = [1, 2, 3, 1]
	print solution.removeElement(li1, 1), li1
	li1 = [1, 2, 3, 1]
	print solution.removeElement(li1, 2), li1
	li1 = [1, 2, 3, 1]
	print solution.removeElement(li1, 3), li1
	li = []
	print solution.removeElement(li, 3), li

