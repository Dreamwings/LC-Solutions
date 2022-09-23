# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float('-inf')
        
        def dfs(node):
            
            if not node: return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            lmax = max(0, l)
            rmax = max(0, r)
            
            self.res = max(self.res, lmax + node.val + rmax)
            
            return node.val + max(lmax, rmax)
        
        dfs(root)
        
        return self.res
        