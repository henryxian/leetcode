# 299. Bulls and Cows

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if secret == "" or guess == "":
        	return "0A0B"
        count_A = 0
        count_B = 0
        map = {}
        for s in secret:
        	if map.get(s) == None:
        		map[s] = 0
        size = len(secret)
        for i in range(size):
        	if secret[i] == guess[i]:
        		count_A = count_A + 1
        	else:
        		if map[guess[i]] == 0:
        			count_B = count_B + 1
        			map[guess[i]] = map[guess[i]] + 1
        return str(count_A) + "A" + str(count_B) + "B" 
