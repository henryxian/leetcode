# Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        table = {}
        for num in nums:
            value = table.get(num)
            if value == None:
                table[num] = num
            else:
                return True
        return False
        