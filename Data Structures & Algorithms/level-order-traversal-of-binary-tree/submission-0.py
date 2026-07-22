# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        def bfs(queue):
            nonlocal res
            if not queue:
                return
            level_res = []
            while queue:
                node = queue.popleft()
                if node:
                    level_res.append(node)
            vals = []
            for node in level_res:
                queue.append(node.left)
                queue.append(node.right)
                vals.append(node.val)
            if vals:
                res.append(vals)
            bfs(queue)
        bfs(queue)
        return res
