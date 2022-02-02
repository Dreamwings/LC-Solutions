# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head: return None
        
        # count number of nodes in the list
        p, n = head, 0
        while p:
            n += 1
            p = p.next
        
        self.x = head
        
        def dfs(l, r):
            if l > r: return
            
            m = (l + r) >> 1
            root = TreeNode()
            root.left = dfs(l, m - 1)
            root.val = self.x.val
            self.x = self.x.next
            root.right = dfs(m + 1, r)
            return root
        
        return dfs(0, n-1)