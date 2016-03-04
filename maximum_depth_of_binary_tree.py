# Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_left = 0
        max_right = 0
        max = 0
        if root == None:
            return 0
        else:
            if root.left == None and root.right == None:
                return 1
            if root.left != None:
                max_left = 1 + self.maxDepth(root.left)
            if root.right != None:
                max_right =  1 + self.maxDepth(root.right)
        max = max_left if max_left > max_right else max_right
        return max