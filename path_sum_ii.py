#  Path Sum II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def path(root, sum, curr, stack, result):
        	curr = curr + root.val
        	stack.append(root.val)
        	isLeaf = not root.left and not root.right
        	if curr == sum and isLeaf:
        		result.append(stack[:])
        		print stack
        		print result
        	if root.left != None:
        		path(root.left, sum, curr, stack, result)
        	if root.right != None:
        		path(root.right, sum, curr, stack, result)
        	stack.pop()
        	print result
        	
        if root == None:
        	return []
        else:
        	stack = []
        	result = []
        	path(root, sum, 0, stack, result)
        	return result