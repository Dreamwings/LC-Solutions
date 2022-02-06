# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ## S2:
        
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next= slow.next.next
        return dummy.next
        
        
        """
        if not head: return None
        
        fast = slow = head
        
        # let fast pointer to move n step first
        
        for _ in range(n):
            if fast:
                fast = fast.next
        
        if not fast: return head.next
        # this can handle the case: head = [1], n = 1, why?
        
        while fast.next:
            # print(slow.val, fast.val)
            fast = fast.next
            slow = slow.next
            
        # print(slow.val)
        slow.next = slow.next.next
        
        return head
        """