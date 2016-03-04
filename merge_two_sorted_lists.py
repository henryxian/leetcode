# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
        	return None
        else:
        	dummy = ListNode(None)
        	curr1 = l1
        	curr2 = l2
        	# dummy.next = l1 if l1.val < l2.val else l2
        	curr = dummy
        	while curr1 and curr2:
        		if curr1.val < curr2.val:
        			curr.next = curr1
        			curr = curr.next
        			curr1 = curr1.next
        		else:
        			curr.next = curr2
        			curr = curr.next
        			curr2 = curr2.next
        	if curr1 != None:
        		curr.next = curr1
        	if curr2 != None:
        		curr.next = curr2
        	return dummy.next