# Isomorphic Strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        kv = {}
        word_set = set()
        index = 0
        for c in s:
        	v = kv.get(c)
        	if v is None:
        		tmp = t[index]
        		if tmp not in word_set:
        			word_set.add(tmp)
        			kv[c] = tmp
        		else:
        			return False
        	else:
        		if v != t[index]:
        			return False
        	index = index + 1
        return True

if __name__ == '__main__':
	solution = Solution()
	# True
	print solution.isIsomorphic("egg", "add")
	# False
	print solution.isIsomorphic("foo", "bar")
	# True
	print solution.isIsomorphic("paper", "title")
	# False
	print solution.isIsomorphic("abcdef", "bbbbbb")
	# True
	print solution.isIsomorphic("abba", "baab")

