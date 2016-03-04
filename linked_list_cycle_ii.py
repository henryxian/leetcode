# 142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def existCycle(head):
	        slow = head
	        fast = head
	        while fast != None and fast.next != None:
	        	slow = slow.next
	        	fast = fast.next.next
	        	if slow == fast:
	        		return slow
	        return None

	    if head == None:
	    	return head
	    else:
	    	fast = existCycle(head)
	    	if fast == None:
	    		return None
	    	else:
	    		slow = head
	    		while slow != fast:
	    			slow = slow.next
	    			fast = fast.next
	    	return slow