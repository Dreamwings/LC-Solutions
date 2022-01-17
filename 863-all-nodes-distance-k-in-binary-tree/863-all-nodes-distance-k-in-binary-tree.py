# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        from collections import defaultdict
        
        ## S1: DFS + DFS Backtracking
        ## find parent nodes and store in dict, then do DFS backtracking
        
        if not root: return []
        
        # dict for parent nodes, key: value = node.val : parent
        p = collections.defaultdict(TreeNode)
        
        def find_parent(node):
            if node.left:
                p[node.left.val] = node
                find_parent(node.left)
            if node.right:
                p[node.right.val] = node
                find_parent(node.right)
        
        find_parent(root)
        
        # now using dfs with backtracking to find nodes with dist k
        
#         def dfs(cur_node, pre_node, k):
#             if k == 0:
#                 res.append(cur_node.val)
#                 return
#             # look at left child
#             if cur_node.left and cur_node.left != pre_node: # not visited
#                 dfs(cur_node.left, cur_node, k - 1)
#             # look at right child
#             if cur_node.right and cur_node.right != pre_node: # not visited
#                 dfs(cur_node.right, cur_node, k - 1)
#             # look at parent
#             if cur_node.val in parents and parents[cur_node.val] != pre_node:
#                 dfs(parents[cur_node.val], cur_node, k - 1)
#         res = []
#         dfs(target, None, k)
        
        def dfs(node, k):
            if k == 0:
                res.append(node.val)
                return
            
            seen.add(node)
            
            if node.left and node.left not in seen:
                dfs(node.left, k - 1)
            if node.right and node.right not in seen:
                dfs(node.right, k - 1)
            if node.val in p and p[node.val] not in seen:
                dfs(p[node.val], k - 1)
            
        res, seen = [], set()
        dfs(target, K)
        
        return res
        
        
        """
        ## S2: DFS + BFS
        
        if root is None: return []
        
        graph = defaultdict(list)
        ## DFS to build graph
        q = [root]
        
        while q:
            node = q.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        
        ## BFS to traverse
        seen = set([target.val])
        cur = [target.val]
        
        for _ in range(K):
            nxt = []
            for y in cur:
                for z in graph[y]:
                    if z not in seen:
                        seen.add(z)
                        nxt.append(z)
            cur = nxt
        
        return cur
        """
        
        