# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        d = collections.Counter()
        res = []
        
        def dfs(node):
            if not node: return '#'
            a = [str(node.val), dfs(node.left), dfs(node.right)]
            key = ','.join(a)
            d[key] += 1
            if d[key] == 2:
                res.append(node)
            return key
        
        dfs(root)
        return res
        