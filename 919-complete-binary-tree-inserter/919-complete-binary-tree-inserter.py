# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.d = {}
        n = 1
        queue = [root]
        while queue:
            node = queue.pop(0)
            self.d[n] = node
            n += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        i = len(self.d) + 1
        self.d[i] = TreeNode(val)
        father = self.d[i//2]
        if i % 2 == 0:
            father.left = self.d[i]
        else:
            father.right = self.d[i]
        
        return father.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.d[1]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()