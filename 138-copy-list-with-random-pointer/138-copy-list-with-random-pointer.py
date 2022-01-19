"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        
        from collections import defaultdict
        
        if not head: return None
        # d = defaultdict(lambda: Node(0, next, random))
        d = defaultdict(lambda: Node(0, None, None))
        d[None] = None  # IMPORTANT, MUST HAVE!
        x = head
        
        while x:
            d[x].val = x.val
            d[x].next = d[x.next]
            d[x].random = d[x.random]
            x = x.next
        
        return d[head]
        
        """
        
        if not head: return None
        d = {}
        x = y = head
        
        while x:
            d[x] = Node(x.val, None, None)
            x = x.next
        
        while y:
            if y.next:
                d[y].next = d[y.next]
            if y.random:
                d[y].random = d[y.random]
            y = y.next
        
        return d[head]
        """
        
