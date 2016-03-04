# Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = dummy.next
        while curr != None:
        	if curr.val == val:
        		prev.next = curr.next
        		curr = prev.next
        	else:
        		prev = prev.next
        		curr = curr.next
        return dummy.next


if __name__ == '__main__':
	solution = Solution()
	solution.removeElements()