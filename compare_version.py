# Compare Version Numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v_1 = version1.split(".")
        v_2 = version2.split(".")
        len1 = len(v_1)
        len2 = len(v_2)
        min_len = len1 if len1 < len2 else len2
        for i in range(min_len):
            if int(v_1[i]) < int(v_2[i]):
                return -1
            if int(v_1[i]) > int(v_2[i]):
                return 1
        if len1 == len2:
            return 0
        elif len1 > len2:
            for i in range(min_len, len1):
                if int(v_1[i]) != 0:
                    return 1
            return 0
        else:
            for i in range(min_len, len2):
                if int(v_2[i]) != 0:
                    return -1
            return 0