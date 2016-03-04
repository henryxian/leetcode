# Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = None
        if p == None or q == None:
        	return None
        if root == None:
        	return None
        else:
        	min = p.val if p.val < q.val else q.val
        	max = p.val if p.val > q.val else q.val
        	if min == root.val or max == root.val:
        		ancestor = root
        	if min < root.val and max > root.val:
        		ancestor = root
        	if max < root.val:
        		ancestor = self.lowestCommonAncestor(root.left, p, q)
        	if min > root.val:
        		ancestor = self.lowestCommonAncestor(root.right, p, q)
        	return ancestor
