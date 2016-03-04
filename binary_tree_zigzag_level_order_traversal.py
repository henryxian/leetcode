# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        else:
        	LEFT_TO_RIGHT = True
        	from collections import deque
        	queue = deque([])
        	result = []
        	queue.append(root)
        	direction = LEFT_TO_RIGHT
        	while len(queue):
        		level_list = []
        		size = len(queue)
        		for i in range(queue):
        			curr = queue.popleft()
        			level_list.append(curr.val)
        			if curr.left:
        				queue.append(curr.left)
        			if curr.right:
        				queue.append(curr.right)
        		if direction == LEFT_TO_RIGHT:
        			result.append(level_list)
        		else:
        			result.append(level_list[::-1])
        		direction = not direction
        	return result

