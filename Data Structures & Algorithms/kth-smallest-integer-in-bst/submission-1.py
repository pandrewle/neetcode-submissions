# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store = []
        def dfs(root):
            nonlocal store
            if not root:
                return False
            if dfs(root.left):
                store.append(root.left.val)
            store.append(root.val)
            if dfs(root.right):
                store.append(root.right.val)
            return False
        dfs(root)
        return store[k-1]
            
            