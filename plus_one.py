# Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = ""
        li = []
        for i in digits:
            digits_str = digits_str + str(i)
        num = int(digits_str)
        num = num + 1
        digits_str = str(num)
        for i in digits_str:
            li.append(int(i))
        return li
        