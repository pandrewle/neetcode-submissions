# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        def dfs(root, maxVal):
            nonlocal res
            if not root:
                return
            left = root.left
            right = root.right
            l_maxVal, r_maxVal = maxVal, maxVal
            if left and left.val >= maxVal:
                l_maxVal = left.val
                res += 1
            if right and right.val >= maxVal:
                r_maxVal = right.val
                res += 1
            dfs(left, l_maxVal)
            dfs(right, r_maxVal)
            return
        dfs(root, root.val)
        return res
