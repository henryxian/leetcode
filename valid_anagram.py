# Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(s) == 0 and len(t) == 0:
            return True
        tb = {}
        for i in s:
            if tb.get(i) == None:
                tb[i] = 1
            else:
                tb[i] = tb[i] + 1
        tb2 = {}
        for i in t:
            if tb2.get(i) == None:
                tb2[i] = 1
            else:
                tb2[i] = tb2[i] + 1
        for i in tb.keys():
            if i in tb2:
                if tb[i] != tb2[i]:
                    return False
            else:
                return False
        return True