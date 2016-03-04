# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        table["I"] = 1
        table["V"] = 5
        table["X"] = 10
        table["L"] = 50
        table["C"] = 100
        table["D"] = 500
        table["M"] = 1000
        length = len(s)
        integer = 1
        index = 1
        if length == 1:
            return table[s[0]]
        integer = table[s[0]]
        while index < length:
            if (table[s[index]] < table[s[index - 1]]):
                integer = integer + table[s[index]]
            elif s[index] == s[index - 1]:
                integer = integer + table[s[index]]
            else:
                integer = integer - 2 * table[s[index - 1]] + table[s[index]]
            index = index + 1
        return integer