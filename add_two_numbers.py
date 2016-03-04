# Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getNum(l):
            base = 1
            sum = 0
            while l != None:
                # sum = sum * base + l.val
                sum = sum + l.val * base
                base = base * 10
                l = l.next
            return sum
        
        def genLinkedList(str):
            dummy = ListNode(None)
            for s in str:
                node = ListNode(int(s))
                node.next = dummy.next
                dummy.next = node
            return dummy.next

        if l1 == None or l2 == None:
            return None
        else:
            num1 = getNum(l1)
            num2 = getNum(l2)
            num = num1 + num2
            return genLinkedList("".join((str(num))))

