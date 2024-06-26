# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        ## S1: DFS
        
        def dfs(x):
            if not x:
                return None, 0
            
            l, l_depth = dfs(x.left)
            r, r_depth = dfs(x.right)
            
            if l_depth > r_depth:
                return l, l_depth + 1
            elif l_depth < r_depth:
                return r, r_depth + 1
            else:
                return x, l_depth + 1
        
        res, _ = dfs(root)
        return res
            