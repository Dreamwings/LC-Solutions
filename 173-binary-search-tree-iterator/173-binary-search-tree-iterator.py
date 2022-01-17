# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = []
        self.inorder(root)
        self.i = 0
        self.n = len(self.data)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.data.append(node.val)
            self.inorder(node.right)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext:
            self.i += 1
            return self.data[self.i-1]
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.i < self.n

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()