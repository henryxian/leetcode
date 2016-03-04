# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
        	return True
        else:
        	dummy = ListNode(None)
        	dummy.next = head
        	prev = dummy
        	#curr = head
        	slow = head
        	fast = head
        	while fast.next and fast.next.next:
        		fast = fast.next.next
        		tmp = slow.next
        		slow.next = prev
        		slow = slow.next
        		prev = slow
        		
        
