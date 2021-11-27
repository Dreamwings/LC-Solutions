# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        ## S1: BFS
        ## Note there are mistakes in the problem:
        ## 1. m = height
        ## 2. for node at (r, c), its left child is at (r+1, c - 2**(h - r - 2))
        ## and its right child is at (r+1, c + 2**(h - r - 2))
        
        def height(root):
            if not root: return 0
            return 1 + max(height(root.left), height(root.right))
        
        # if not root: return ['']
        m = height(root)
        n = 2**m - 1
        res = [[''] * n for _ in range(m)]
        
        r, c = 0, (n-1)//2
        q = [(root, c)]
        
        while q:
            nxt = []
            for x, c in q:
                res[r][c] = str(x.val)
                if x.left:
                    nxt.append((x.left, c - 2**(m - r - 2)))
                if x.right:
                    nxt.append((x.right, c + 2**(m - r - 2)))
            r += 1
            q = nxt
        return res