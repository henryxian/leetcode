# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.kth = k
        
        def find_kth(node):
            target = None
            if node.left:
        		target = find_kth(node.left)
            if target == None:
                #if self.kth == 1:
                #    target = node 
                #self.kth = self.kth - 1
                self.kth = self.kth - 1
                if self.kth == 0:
                    target = node
            if target == None and node.right:
                target = find_kth(node.right)
            return target
        
        result = find_kth(root)
        return result.val     