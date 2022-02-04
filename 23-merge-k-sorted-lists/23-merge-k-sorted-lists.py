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
        
        from heapq import heapify, heappush, heappop
        
        hq = []
        for i, node in enumerate(lists):
            if node:
                hq.append((node.val, i, node))  # add index i to avoid heapq comparison error between nodes with same values
        
        heapify(hq)
        dummy = curr = ListNode(0)
        
        while hq:
            v, i, x = heappop(hq)
            curr.next = x
            curr = curr.next
            
            if x.next:
                heappush(hq, (x.next.val, i, x.next))
        
        return dummy.next
            
        
        