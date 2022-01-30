"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return None
        
        q = [root]
        
        while q:
            q.append(None)
            nxt = []
            for x, y in zip(q[:-1], q[1:]):
                x.next = y
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            q = nxt
        
        return root