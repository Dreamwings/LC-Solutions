# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head.next: return head
        
        p = head
        
        while p and p.next:
            # print(p.val, head.val)
            p = p.next.next
            head = head.next
            
        return head