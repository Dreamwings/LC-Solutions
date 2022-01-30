"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
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