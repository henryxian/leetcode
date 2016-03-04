# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        offset = n - 1
        ptr_end = head
        ptr_end_nth = head
        dummy = ListNode(1)
        prev = dummy
        prev.next = ptr_end_nth
        while offset:
            ptr_end = ptr_end.next
            offset = offset - 1
        while ptr_end.next != None:
            prev = prev.next
            ptr_end = ptr_end.next
            ptr_end_nth = ptr_end_nth.next
        prev.next = ptr_end_nth.next
        return dummy.next