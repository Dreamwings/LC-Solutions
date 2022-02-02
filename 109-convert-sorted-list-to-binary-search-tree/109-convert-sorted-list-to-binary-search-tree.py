# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        ## Solution 1:
        
        if not head: return None
        
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        
        self.x = head
        
        def convert(lo, hi):
            if lo > hi: return None
            
            m = (lo + hi) >> 1
            root = TreeNode()
            root.left = convert(lo, m - 1)
            root.val = self.x.val
            self.x = self.x.next
            root.right = convert(m + 1, hi)
            
            return root
        
        return convert(0, n-1)
        
        
        """
        ## Solution 2:
        
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def arrayToBST(arr):
            n = len(arr)
            if n == 0: return None
            if n == 1: return TreeNode(arr[0])
            m = n >> 1
            root = TreeNode(arr[m])
            root.left = arrayToBST(arr[:m])
            root.right = arrayToBST(arr[m+1:])
            return root
        
        return arrayToBST(arr)
        
        
        ## Solution 3:
        
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        root = TreeNode(slow.val)
        prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
        """