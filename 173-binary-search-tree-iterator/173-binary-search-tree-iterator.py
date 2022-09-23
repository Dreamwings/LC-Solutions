# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    from collections import deque
    
    def __init__(self, root: Optional[TreeNode]):
        self.d = deque()
        self.inorder(root)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.d.append(node.val)
            self.inorder(node.right)

    def next(self) -> int:
        if self.hasNext:
            return self.d.popleft()        

    def hasNext(self) -> bool:
        return len(self.d) > 0
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()