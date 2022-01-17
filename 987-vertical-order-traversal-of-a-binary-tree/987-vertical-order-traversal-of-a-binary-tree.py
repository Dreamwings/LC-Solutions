# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        from collections import defaultdict
        
        if not root: return []
        
        d = defaultdict(list)
        res = []
        q = [(root, 0)]
        
        while q:
            nxt = []
            t = defaultdict(list)
            for node, col in q:
                t[col].append(node.val)
                if node.left:
                    nxt.append((node.left, col - 1))
                if node.right:
                    nxt.append((node.right, col + 1))
            
            for k, v in t.items():
                d[k] += sorted(v)
            
            q = nxt
        
        for k in sorted(d):
            res.append(d[k])
        
        return res
        
        
        
        