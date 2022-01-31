# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ## S2: Iterative BFS
        
        res = []
        if not root: return res
        
        q = collections.deque()
        q.append(root)
        
        while q:
            nxt = []
            for node in q:
                x = node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            res.append(x)
            q = nxt
        
        return res
        
        """
        ## S1: Recursive DFS
        
        res = []
        if not root: return res
        
        res.append(root.val)
        
        l = self.rightSideView(root.left)
        r = self.rightSideView(root.right)
        
        res += r
        
        ll, rl = len(l), len(r)
        if rl < ll:
            res += l[rl:]
        
        return res
        """
        