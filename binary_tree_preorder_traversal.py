# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO: 非递归版本
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node, li):
            li.append(node.val)
            if node.left != None:
                helper(node.left, li)
            if node.right != None:
                helper(node.right, li)
            return li
        
        if root == None:
            return []
        else:
            traversal = []
            return helper(root, traversal)
        