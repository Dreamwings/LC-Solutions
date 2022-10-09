# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        def serialize(node):
            if not node:
                return ',#'
            return ',' + str(node.val) + serialize(node.left) + serialize(node.right)
        
        a = serialize(root)
        b = serialize(subRoot)
        
        # print(a)
        # print(b)
        
        return b in a
        
        