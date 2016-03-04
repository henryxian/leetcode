# Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def hasPath(root, sum, curr):
            curr = curr + root.val
            isLeaf = root.left == None and root.right == None
            if curr == sum and isLeaf:
                return True
            if root.left != None:
                l = hasPath(root.left, sum, curr)
            else:
                l = False
            if root.right != None:
                r = hasPath(root.right, sum, curr)
            else:
                r = False
            if l or r:
                return True
            else:
                return False
                
        if root == None:
            return False
        else:
            return hasPath(root, sum, 0)