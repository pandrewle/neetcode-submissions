# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)
        else:
            return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root:
                return False
            elif self.isEqual(root, subRoot):
                return True
            else:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot)