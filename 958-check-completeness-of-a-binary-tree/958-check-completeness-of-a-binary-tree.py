# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        ## Solution 1: DFS
        
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
        ## Solution 2: BFS
        from collections import deque
        
        if root is None: return True
        
        res = []
        q = deque([(root, 1)])
        
        while q:
            node, i = q.popleft()
            res.append(i)
            if node.left:
                q.append((node.left, 2 * i))
            if node.right:
                q.append((node.right, 2 * i + 1))
        
        return res[-1] == len(res)
        
        
        ## Solution 3: BFS (Improved Solution 2)
        from collections import deque
        
        if root is None: return True
        
        num = 0
        q = deque([(root, 1)])
        
        while q:
            node, i = q.popleft()
            num += 1
            if node.left:
                q.append((node.left, 2 * i))
            if node.right:
                q.append((node.right, 2 * i + 1))
        
        return num == i
        """