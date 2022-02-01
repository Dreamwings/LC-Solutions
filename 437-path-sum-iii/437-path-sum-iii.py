# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict
        
        ## S1: DFS
        ## Time: O(N)
        ## Space: O(N)
        
        if not root: return 0
        
        d = defaultdict(int)
        d[0] = 1
        
        def dfs(node, pre_sum, t):
            if not node: return 0
            cnt = 0
            cur_sum = pre_sum + node.val
            diff = cur_sum - t
            if diff in d: # there's at least one path with sum of diff already
                cnt += d[diff]
            
            d[cur_sum] += 1 # if cur_sum previously not in d, d[cur_sum] = 0
            
            cnt += dfs(node.left, cur_sum, t)
            cnt += dfs(node.right, cur_sum, t)
            
            d[cur_sum] -= 1
            # because this "node" is not on other paths, after the DFS with 
            # paths containing it, it needs to be removed from the record
            return cnt
                
        return dfs(root, 0, targetSum)        
            
        """
        
        ## S2: DFS
        ## Time: O(N^2)
        ## Space: O(N)
        
        
        def dfs(root, t):
            if not root: return 0
            
            cnt = 0
            if root.val == t:
                cnt += 1
                
            cnt += dfs(root.left, t - root.val)
            cnt += dfs(root.right, t - root.val)
            return cnt
        
        if not root: return 0
        res = dfs(root, targetSum)  # number of all paths starting from root
        res += self.pathSum(root.left, targetSum)   # number of all paths for left subtree
        res += self.pathSum(root.right, targetSum)  # number of all paths for right subtree
        return res
        
        """
