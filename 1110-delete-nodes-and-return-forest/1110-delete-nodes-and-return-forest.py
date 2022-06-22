# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        to_del = set(to_delete)
        res = []
        
        def dfs(node):
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                if node.val in to_del:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)
                    return None
                else:
                    return node
                
        if root.val not in to_del:
            res.append(root)
        
        dfs(root)
        return res