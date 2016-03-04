# count and say

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def gen_seq(seq):
            index = 1
            size = len(seq)
            prev = seq[0]
            count = 1
            tmp = ""
            while index < size:
                if prev == seq[index]:
                    count = count + 1
                else:
                    tmp = tmp + str(count) + prev
                    prev = seq[index]
                    count = 1
                index = index + 1
            tmp = tmp + str(count) + prev
            return tmp

        if n <= 0:
            return "1"
        seq = "1"
        if n == 1:
            return seq
        else:
            result = gen_seq(seq)
            n = n - 2
            while n:
                result = gen_seq(result)
                n = n - 1
            return result

if __name__ == '__main__':
	solution = Solution()
	print solution.countAndSay(3)
	print solution.countAndSay(6)