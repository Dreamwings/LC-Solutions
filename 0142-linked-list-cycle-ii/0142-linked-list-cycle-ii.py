# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Solution 1:
        ## Time: O(N)
        ## Space: O(N)
        
        seen = set()
        p = head
        
        while p:
            if p in seen:
                return p
            else:
                seen.add(p)
                p = p.next
        return None
        
        """
        
        ## Solution 2:
        
#         Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
#         H: distance from head to cycle entry E
#         D: distance from E to X
#         L: cycle length
#                           __________
#                          /          \D
#         head_____H______E            \
#                         \            /
#                          \____X_____/   
#                              slow
    
#         If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
#         Assume fast has traveled n loops in the cycle, we have:
#         2(H + D) = H + D + nL  -->  
#         H + D = nL  --> 
#         H = nL - D
#         let n = 1, we have: 
#         H = L - D (from head to E = from X to E)
        
        # to check if it has a circle
        
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:  # while-else usage
            return None
        
        # from head to E has the same distance as from X to E
        while head != slow:
            head = head.next
            slow = slow.next
        
        return head
        
        """
        
        