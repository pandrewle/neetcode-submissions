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
        if not p and q or p and not q:
            return False
        if p.val == q.val and self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right):
            return True
        else:
            return False
        return self.isEqual(p, q)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSubtree = False
        def dfs(root, subRoot):
            nonlocal isSubtree
            if not root:
                return False
            elif self.isEqual(root, subRoot):
                isSubtree = True
            else:
                dfs(root.left, subRoot)
                dfs(root.right, subRoot)
        dfs(root, subRoot)
        return isSubtree