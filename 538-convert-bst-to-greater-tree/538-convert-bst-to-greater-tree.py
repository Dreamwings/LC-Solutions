# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        ## S1: Reverse inorder traversal
        
        self.s =  0
        
        def dfs(node):
            if node:
                dfs(node.right)
                self.s += node.val
                node.val = self.s
                dfs(node.left)
        
        dfs(root)
        return root