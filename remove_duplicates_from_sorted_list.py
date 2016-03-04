# Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return None
        dummy = head
        prev = head
        curr = head.next
        while curr != None:
        	if prev.val == curr.val:
        		prev.next = curr.next
        		curr = prev.next
        	else:
        		prev = prev.next
        		curr = curr.next
        return dummy