# 303. Range Sum Query - Immutable

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = []

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def numArray():
	    	index = 1
	    	length = len(nums)
	    	self.sum.append(self.nums[0])
	    	while index < length:
	    		self.sum.append(self.sum[-1] + self.nums[index])
	    		index = index + 1

        numArray()
        if i > j or i < 0 or j < 0 or i > len(nums) or j > len(nums):
        	return 0
        else:
        	if i == j:
        		return self.nums[i]
        	else:
        		return self.sum[j] - self.sum[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
if __name__ == '__main__':
	# nums = [1, 1, 2, 2, 3]
	# numArray = NumArray(nums)
	# print numArray.sumRange(0, 1)
	# print numArray.sumRange(1, 2)
	# print numArray.sumRange(0, 4)
	# print numArray.sumRange(4, 4)
	# print numArray.sumRange(0, -1)
	# print numArray.sumRange(1, 1)

	# nums = [-1]
	# numArray = NumArray(nums)
	# print numArray.sumRange(0, 0)

	nums = [5824,4501,7189,-5915,2775,-5070,4865,-5204]
	numArray = NumArray(nums)
	sumRange = numArray.sumRange
	print sumRange(0,1)
	print sumRange(6,7)
	print sumRange(0,7)
	print sumRange(3,4)
	print sumRange(1,4)
	print sumRange(3,5)
	print sumRange(2,6)
	print sumRange(4,5)
	print sumRange(3,7)
	print sumRange(2,4)
	print sumRange(5,5)
	print sumRange(3,6)
	print sumRange(0,2)
	print sumRange(4,6)
	print sumRange(3,6)
	print sumRange(0,2)
	print sumRange(4,4)
	print sumRange(3,3)
	print sumRange(3,5)
	print sumRange(2,5)
	print sumRange(7,7)
	print sumRange(5,6)
	print sumRange(4,5)
	print sumRange(6,6)
	
