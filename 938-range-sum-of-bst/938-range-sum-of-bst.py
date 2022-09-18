# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        from collections import deque
        
        q = deque()
        q.append(root)
        res = 0
        
        while q:
            x = q.popleft()
            if low <= x.val <= high:
                res += x.val
            if x.val > low and x.left:
                q.append(x.left)
            if x.val < high and x.right:
                q.append(x.right)
        
        return res
        
        
        