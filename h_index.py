# 274. H-Index

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        if size == 0:
            return 0
        if size == 1 and citations[0] != 0:
            return 1
        sorted_cita = sorted(citations, reverse=True)
        for i in range(0, size):
            if i >= sorted_cita[i]:
                return i
        if size - 1 < sorted_cita[size - 1]:
            return size
        return 0
        
        