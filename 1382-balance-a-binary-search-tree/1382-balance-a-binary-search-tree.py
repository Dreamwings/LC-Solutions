# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        ## S2: Store nodes instead of node.val
        ## Time: O(N)
        ## Space: O(N)
        
        def in_order(root):
            if not root: return []
            return in_order(root.left) + [root] + in_order(root.right)
        
        nodes = in_order(root)
        
        def build_bst(l, r):  # use l, r pointers instead of array slicing can save memory
            if l > r: return None
            m = (l + r) // 2
            root = nodes[m]
            root.left = build_bst(l, m-1)
            root.right = build_bst(m+1, r)
            return root
        
        return build_bst(0, len(nodes)-1)
        
        """
        ## S1: 
        ## Time: O(N)
        ## Space: O(N)
        
        def in_order(root):
            if not root: return []
            return in_order(root.left) + [root.val] + in_order(root.right)
        
        vals = in_order(root)
        
        def build_bst(l, r):  # use l, r pointers instead of array slicing can save memory
            if l > r: return None
            
            m = (l + r) // 2
            root = TreeNode(vals[m])
            root.left = build_bst(l, m-1)
            root.right = build_bst(m+1, r)
            return root
        
        return build_bst(0, len(vals)-1)
        
        """
        
