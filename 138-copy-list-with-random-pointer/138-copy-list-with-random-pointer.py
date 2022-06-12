"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        from collections import defaultdict
        
        if not head: return None
        
        d = defaultdict(lambda: Node(0, None, None))
        d[None] = None
        x = head
        
        while x:
            d[x].val = x.val
            d[x].next = d[x.next]
            d[x].random = d[x.random]
            x = x.next
            
        return d[head]