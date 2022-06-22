# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        d = set(to_delete)
        res = []
        
        def dfs(node):
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                if node.val in d:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)
                    return None
                else:
                    return node
                
        if root.val not in d:
            res.append(root)
            
        dfs(root)
        return res