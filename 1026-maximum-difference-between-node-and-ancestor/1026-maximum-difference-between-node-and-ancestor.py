# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ## S1: DFS
        
        self.res = 0
        
        def dfs(node):
            if not node:
                return float('-inf'), float('inf')
            
            lmax, lmin = dfs(node.left)
            rmax, rmin = dfs(node.right)
            
            cur_max = max(lmax, rmax, node.val)
            cur_min = min(lmin, rmin, node.val)
            
            self.res = max(self.res, node.val - cur_min, cur_max - node.val)
            
            return cur_max, cur_min
        
        dfs(root)
        return self.res
        
        