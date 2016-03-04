# binary tree level order traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if root == None:
        	return []
        else:
            stack = []
            queue = deque([])
            queue.append(root)
            while len(queue) != 0:
                level_list = []
                size = len(queue)
                for i in range(size):
                    curr = queue.popleft()
                    level_list.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                stack.append(level_list)
            return stack[::-1]
        	