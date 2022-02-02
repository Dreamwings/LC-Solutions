# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        ## Solution 2:
        
        if not root: return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, lower, upper = stack.pop()
            if node.val <= lower or node.val >= upper:
                return False
            if node.left:
                stack.append((node.left, lower, node.val))
            if node.right:
                stack.append((node.right, node.val, upper))
        
        return True
        
        """
        ## Solution 1: O(N)
        
        if not root: return True
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        vals = inorder(root)
        
        for i in range(1, len(vals)):
            if vals[i] <= vals[i-1]:
                return False
            
        return True
        
        """
        
        