# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def dfs(root):
            if not root:
                self.res.append('null#')
                return
            self.res.append(str(root.val) + '#')
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return ''.join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = 0
        def dfs(idx, data):
            val = ''
            while self.idx < len(data)-1 and data[self.idx] != '#':
                val += data[self.idx]
                self.idx += 1
            self.idx += 1
            if val == 'null':
                return None
            root = TreeNode(int(val))
            root.left = dfs(self.idx, data)
            root.right = dfs(self.idx, data)
            return root
        return dfs(self.idx, data)
