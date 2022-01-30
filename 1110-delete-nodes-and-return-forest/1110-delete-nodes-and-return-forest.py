# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        to_del = set(to_delete)
        res = []
        
        def dfs(node):
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                if node.val in to_del:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)
                    return None
                
                return node
        
        if root.val not in to_del:
            res.append(root)
            
        dfs(root)
        return res