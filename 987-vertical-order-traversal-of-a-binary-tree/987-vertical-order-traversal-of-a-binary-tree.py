# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import defaultdict
        
        if not root: return []
        
        d = defaultdict(list)
        res = []
        q = [(root, 0)]
        
        while q:
            nxt = []
            t = defaultdict(list)
            for node, i in q:
                t[i].append(node.val)
                if node.left:
                    nxt.append((node.left, i-1))
                if node.right:
                    nxt.append((node.right, i+1))
            
            q = nxt
            for k, v in t.items():
                d[k] += sorted(v)
        
        for k in sorted(d):
            res.append(d[k])
        
        return res