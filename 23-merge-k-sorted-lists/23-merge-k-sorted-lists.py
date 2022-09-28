# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        from heapq import heappush, heappop, heapify
        
        # if not lists: return None
        hq = []
        
        for i, node in enumerate(lists):
            if node:
                heappush(hq, (node.val, i, node))
        
        dummy = ListNode(0)
        p = dummy
        
        while hq:
            v, i, node = heappop(hq)
            p.next = node
            p = p.next
            if node.next:
                heappush(hq, (node.next.val, i, node.next))
        
        return dummy.next
            
        