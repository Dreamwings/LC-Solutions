# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(node):
            if not node: return None
            pre, cur = None, node
            
            while cur:
                cur.next, cur, pre = pre, cur.next, cur
            
            return pre
        
        if not head: return True
        fast = slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        half2 = slow.next
        slow.next = None
        
        half1, half2 = head, reverse(half2)
        
        while half1 and half2:
            if half1.val != half2.val:
                return False
            half1 = half1.next
            half2 = half2.next
            
        return True