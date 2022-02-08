# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        d = collections.Counter()
        res = []
        
        def dfs(node):
            if not node: return '#'
            key = '{}, {}, {}'.format(node.val, dfs(node.left), dfs(node.right))
            d[key] += 1
            if d[key] == 2:
                res.append(node)
            return key
        
        dfs(root)
        return res
        