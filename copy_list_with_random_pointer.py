# copy list with random pointer

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
        	return head
        map = {}
        cloned_head = RandomListNode(head.label)
        curr_cloned = cloned_head
        curr = head
        map[head] = cloned_head
        while curr.next != None:
        	tmp_node = RandomListNode(curr.next.label)
        	curr_cloned.next = tmp_node
        	map[curr.next] = curr_cloned.next
        	curr = curr.next
        	curr_cloned = curr_cloned.next
        #curr_cloned.next = None
        curr = head
        while curr != None:
        	if curr.random == None:
        		map[curr].random = None
        	else:
        		map[curr].random = map[curr.random]
        	curr = curr.next
        return cloned_head