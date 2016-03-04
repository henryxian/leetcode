# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        lenA = 0
        lenB = 0
        currA = headA
        currB = headB
        while currA != None:
            currA = currA.next
            lenA = lenA + 1
        while currB != None:
            currB = currB.next
            lenB = lenB + 1
        if lenA < lenB:
            n = lenB - lenA
            currB = headB
            while n:
                currB = currB.next
                n = n - 1
        else:
            n = lenA - lenB
            currA = headA
            while n:
                currA = currA.next
                n = n - 1
            while currA != None:
                if currA == currB:
                    return currA
                else:
                    currA = currA.next
                    currB = currB.next
            return None

