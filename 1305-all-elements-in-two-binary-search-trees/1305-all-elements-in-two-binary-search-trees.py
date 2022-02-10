# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        ## S1: Inorder Traversal and Merge
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        a = inorder(root1)
        b = inorder(root2)
        res = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        
        res += a[i:] + b[j:]
        return res
            
        """
        
        ## S2: Inorder Traversal and Timsort
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        a = inorder(root1)
        b = inorder(root2)
        
        return sorted(a + b)