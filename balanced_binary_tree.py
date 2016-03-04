# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO: 用后序遍历的方法再做一遍
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def treeDepth(root):
            left = 0
            right = 0
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1
            if root.left != None:
                left = 1 + treeDepth(root.left)
            if root.right != None:
                right = 1 + treeDepth(root.right)
            return max(left, right)
            
        if root == None:
            return True
        else:
            left = treeDepth(root.left)
            right = treeDepth(root.right)
            if abs(left - right) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)