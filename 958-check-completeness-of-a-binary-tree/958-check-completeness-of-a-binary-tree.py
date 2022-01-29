# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        ## S1: DFS
        
        if not root: return True
        
        def dfs(node, i):
            # return total number of nodes and the index of the far right node at the last level
            if not node: return (0, 0)
            
            l_cnt, l_last = dfs(node.left, 2 * i)
            r_cnt, r_last = dfs(node.right, 2 * i + 1)
            
            cnt = l_cnt + r_cnt + 1
            last = max(i, l_last, r_last)
            
            return (cnt, last)
        
        cnt, last = dfs(root, 1)
        return cnt == last
        
        
        """
        ## BFS
        from collections import deque
        
        q = deque([(root, 1)])
        cnt = 0
        
        while q:
            node, x = q.popleft()
            cnt += 1
            if node.left:
                q.append((node.left, 2 * x))
            if node.right:
                q.append((node.right, 2 * x + 1))
        
        if x == cnt:
            return True
        return False
            
        """
        
        