# insertion sort list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
        	dummy = ListNode(None)
        	dummy.next = head
        	curr = head.next
        	prev = dummy
        	index = prev.next
        	while curr != None:
        		if curr.val < index:
        			

        			
        else:
        	return head
