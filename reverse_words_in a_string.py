# 151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitted = s.split()
        rev_str = ""
        if len(splitted):
            rev = splitted[::-1]
            for word in rev:
                rev_str = rev_str + " " + word
            rev_str = rev_str.strip()
        return rev_str