# Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        index1 = 0
        index2 = 0
        index = 0
        length = len(nums)
        while index < length:
        	if nums[index] == 0:
        		count = count + 1
        	index = index + 1
        while index1 < length:
        	if nums[index1] != 0:
        		nums[index2] = nums[index1]
        		index1 = index1 + 1
        		index2 = index2 + 1
        	else:
        		while index1 < length and nums[index1] == 0:
        			index1 = index1 + 1
       	index = length - count
        while index < length:
        	nums[index] = 0
        	index = index + 1

if __name__ == '__main__':
	solution = Solution()
	li1 = [1, 1, 2, 2, 0]
	li2 = [2, 2, 0, 0, 3]
	li3 = [3, 0, 2, 6, 1]
	solution.moveZeroes(li1)
	print li1
	solution.moveZeroes(li2)
	print li2
	solution.moveZeroes(li3)
	print li3