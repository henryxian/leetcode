# Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_left = 0
        min_right = 0
        min = 0
        if root == None:
            return 0
        else:
            if root.left == None and root.right == None:
                return 1
            if root.left != None and root.right == None:
                min_left = 1 + self.minDepth(root.left)
                return min_left
            if root.right != None and root.left == None:
                min_right = 1 + self.minDepth(root.right)
                return min_right
            else:
                min_left = 1 + self.minDepth(root.left)
                min_right = 1 + self.minDepth(root.right)
                min = min_left if min_left < min_right else min_right
                return min