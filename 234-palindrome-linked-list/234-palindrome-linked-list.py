# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(node):
            prev, curr = None, node
            while curr:
                curr.next, curr, prev = prev, curr.next, curr
            
            return prev
        
        if not head: return True
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        tmp, slow.next = slow.next, None
        first = head
        second = reverse(tmp)
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True