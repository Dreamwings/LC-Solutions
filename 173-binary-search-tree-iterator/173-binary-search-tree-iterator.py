# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    from collections import deque
    
    def __init__(self, root: Optional[TreeNode]):
        self.data = deque()
        self.in_order(root)
        
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            self.data.append(node.val)
            self.in_order(node.right)

    def next(self) -> int:
        if self.hasNext:
            return self.data.popleft()
            
        

    def hasNext(self) -> bool:
        return len(self.data) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()