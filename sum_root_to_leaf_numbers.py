# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumN(node, path, sum):
        	sum = sum * 10 + node.val
        	if node.left == None and node.right == None:
        		path.append(sum)
        	if node.left != None:
        		sumN(node.left, path, sum)
        	if node.right != None:
        		sumN(node.right, path, sum)

        if root == None:
			return 0
        else:
			path = []
			sum = 0
			sumN(root, path, sum)
			return reduce(lambda a, b: a + b, path)