# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            div = 1
            while x / div >= 10:
                div = div * 10
            while x != 0:
                l = x / div
                r = x % 10
                if l != r:
                    return False
                x = (x % div) / 10
                div = div / 100
        return True
            