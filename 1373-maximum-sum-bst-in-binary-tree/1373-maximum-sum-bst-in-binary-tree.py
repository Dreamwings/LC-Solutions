# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ## S1: DFS
        ## Time: O(N)
        ## Space: O(H)
        
        MIN, MAX = float('-inf'), float('inf')
        self.res = 0
        
        # DFS function to return the min val of tree, max val of tree, sum of keys
        def dfs(node):
            if not node: return MAX, MIN, 0  # IMPORTANT!!! note NOT (return MIN, MAX, 0)
            
            lmin, lmax, lsum = dfs(node.left)
            rmin, rmax, rsum = dfs(node.right)
            
            # can be a BST with root at node
            if lmax < node.val < rmin:
                cur_sum = lsum + node.val + rsum
                self.res = max(self.res, cur_sum)
                return min(lmin, node.val), max(rmax, node.val), cur_sum
            else:
                return MIN, MAX, 0
        
        dfs(root)
        return self.res
        