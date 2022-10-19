# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node] + inorder(node.right)
        
        nodes = inorder(root)
        
        def build_bst(l, r):
            if l > r: return None
            
            m = (l + r) >> 1
            root = nodes[m]
            root.left = build_bst(l, m - 1)
            root.right = build_bst(m + 1, r)
            return root
        
        return build_bst(0, len(nodes) - 1)