# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        a = inorder(root1)
        b = inorder(root2)
        
        i = j = 0
        res = []
        
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        
        if i < len(a):
            res += a[i:]
        if j < len(b):
            res += b[j:]
        return res