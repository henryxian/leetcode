# Binary Tree Path

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def find_path(node, path, result):
        	path.append(node.val)
        	if not node.left and not node.right:
        		tmp = ""
        		for i in path:
        			tmp = tmp + str(i) + "->" 
        		tmp = tmp[:-2]
        		result.append(tmp)
        	if node.left != None:
        		find_path(node.left, path, result)
        	if node.right != None:
        		find_path(node.right, path, result)
        	path.pop()
        if root == None:
            return []
        else:
        	result = []
        	path = []
        	find_path(root, path, result)
        	return result

