# Odd Even Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy = ListNode(None)
        # dummy2 = ListNode(None)
        # dummy.next = head
        # flag = 0
        # curr_node = dummy.next
        # prev = dummy
        # while curr_node != None:
        #     if flag == 0:
        #         prev = curr_node
        #         curr_node = curr_node.next
        #         flag = 1
        #     else:
        #         prev.next = curr_node.next
        #         curr_node = prev.next
        #         flag = 0
        # return dummy.next
        if head == None:
        	return None
        else:
        	odd_head = head
        	even_head = head.next
        	odd_curr = odd_head
        	even_curr = even_head
        	while odd_curr.next and even_curr.next:
        		odd_curr.next = odd_curr.next.next
        		odd_curr = odd_curr.next
        		even_curr.next = even_curr.next.next
        		even_curr = even_curr.next
        	odd_curr.next = even_head
        	return odd_head
