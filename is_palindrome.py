# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s = s.lower()
        idx_begin = 0
        idx_end = len(s) - 1
        while idx_begin < idx_end:
            while s[idx_begin].isalnum() == False and idx_begin < idx_end:
                idx_begin =idx_begin + 1
                #if idx_begin >= idx_end:
                #   break
            while s[idx_end].isalnum() == False and idx_begin < idx_end:
                idx_end = idx_end - 1
                #if idx_begin >= idx_end:
                #   break
            if s[idx_begin] != s[idx_end]:
                return False
            else:
                idx_begin += 1
                idx_end -= 1
        return True