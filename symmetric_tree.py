# Symmetric Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO stack implementation
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetricHelper(left, right):
            if left == None and right == None:
                return True
            if left != None and right == None:
                return False
            if left == None and right != None:
                return False
            if left.val != right.val:
                return False
            return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
            
        if root == None:
            return True
        else:
            return isSymmetricHelper(root.left, root.right)
            
