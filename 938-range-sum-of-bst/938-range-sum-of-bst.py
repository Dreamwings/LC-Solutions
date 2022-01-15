# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        """
        ## S1: Recursive DFS
        ## Time: O(N)
        ## Space: O(N)
        
        res = 0
        if not root: return res
        
        if low <= root.val <= high:
            res += root.val
        
        l = self.rangeSumBST(root.left, low, high)
        r = self.rangeSumBST(root.right, low, high)
        
        return res + l + r
        
        """
        
        ## S2:  Iterative BFS
        ## Time: O(N)
        ## Space: O(N)
        
        from collections import deque
        
        if not root: return 0
        
        res = 0
        q = deque([root])
        
        while q:
            x = q.popleft()
            if low <= x.val <= high:
                res += x.val
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        
        return res
        
        
        
        