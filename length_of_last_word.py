# Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        if len(word_list) != 0:
        	last = word_list[-1]
        	return len(last)
        else:
        	return 0

if __name__ == '__main__':
	solution = Solution()

	# 0
	print solution.lengthOfLastWord("")
	# 4
	print solution.lengthOfLastWord("henry xian")
	# 0
	print solution.lengthOfLastWord("        ")