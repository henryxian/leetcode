# Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        dummy = ListNode(None)
        dummy.next = head
        curr_node = dummy.next
        hd = None
        while curr_node != None:
            stack.append(curr_node)
            curr_node = curr_node.next
        if len(stack) != 0:
            tail = stack.pop()
            tail.next = None
            hd = tail
        while len(stack) != 0:
            tail.next = stack.pop()
            tail = tail.next
            tail.next = None
        return hd