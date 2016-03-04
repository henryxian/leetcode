class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        index = 0
        sep_list = str.split()
        kv = {}
        for k in pattern:
        	v = kv.get(k)
        	if v is None:
        		kv[k] = sep_list[index]
        	elif kv[k] != sep_list[index]:
        		return False
        	else:
        		pass
        	index = index + 1
        return True

    def wordPattern2(self, pattern, str):
    	index = 0
    	sep_list = str.split()
    	word_set = set()
    	len_pattern = len(sep_list)
    	print len_pattern
    	len_str = len(pattern)
    	print len_str
    	if len_str != len_pattern:
    		return False
    	kv = {}

    	for k in pattern:
    		v = kv.get(k)
    		if v is None:
    			tmp = sep_list[index]
    			if tmp not in word_set:
    				kv[k] = sep_list[index]
    				word_set.add(tmp)
    			else:
    				return False
    		index = index + 1
    	# notice
    	return True
    	# index = 0
    	# for k in pattern:
    	# 	v = kv[k]
    	# 	if v == sep_list[index]:
    	# 		pass
    	# 	else:
    	# 		return False
    	# 	index = index + 1
    	# return True

    def wordPattern3(self, pattern, str):
    	len_pattern = len(pattern)


if __name__ == '__main__':
	solution = Solution()

	# True
	print solution.wordPattern2("abba", "dog cat cat dog")

	# False
	print solution.wordPattern2("abba", "dog cat cat fish")

	# False
	print solution.wordPattern2("aaaa", "dog cat cat dog")

	# False
	print solution.wordPattern2("abba", "dog dog dog dog")

	# True 
	print solution.wordPattern2("bbaa", "dog dog cat cat")

	# False
	print solution.wordPattern2("abcd", "fuck fuck fuck fuck")

	# False
	print solution.wordPattern2("jquery", "jquery")