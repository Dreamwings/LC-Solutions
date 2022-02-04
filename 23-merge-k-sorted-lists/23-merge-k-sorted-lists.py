# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        from heapq import heapify, heappush, heappop
        
        hq = []
        # to avoid error from heapq by comparing two nodes when they have the same values
        for i, node in enumerate(lists):
            if node:
                heappush(hq, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while hq:
            v, i, x = heappop(hq)
            curr.next = x
            curr = curr.next
            
            if x.next:
                heappush(hq, (x.next.val, i, x.next))
        
        return dummy.next
        
        
        """
        # need to redefine the operator to compare ListNode, otherwise Python 3 will report errors
        def __lt__(a: ListNode, b: ListNode):
            return a.val < b.val
        ListNode.__lt__ = __lt__

        
        hq = []
        for node in lists:
            if node:
                hq.append((node.val, node))
        
        heapify(hq)
        dummy = ListNode(0)
        curr = dummy
        
        while hq:
            v, x = heappop(hq)
            curr.next = x
            curr = curr.next
            if x.next:
                heappush(hq, (x.next.val, x.next))
            
        return dummy.next
        """
        
        
        