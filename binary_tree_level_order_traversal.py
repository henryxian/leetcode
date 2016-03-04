# Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        queue = deque([])
        result = []
        if root == None:
            return result
		else:
			queue.append(root)
			while len(queue):
				level_list = []
				# 用size记录当前层的节点个数
				size = len(queue)	  		# very tricky here 
				for i in range(size): 		# very tricky here
					curr = queue.popleft()
					level_list.append(curr.val)
					if curr.left:
						queue.append(curr.left)
					if curr.right:
						queue.append(curr.right)
				result.append(level_list)
			return result
