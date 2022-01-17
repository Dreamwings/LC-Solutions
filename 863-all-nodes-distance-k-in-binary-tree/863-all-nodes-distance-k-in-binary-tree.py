# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        ## S1: DFS + DFS Backtracking
        ## find parent nodes and store in dict, then do DFS backtracking
        
        if not root: return []
        
        # dict for parent nodes, key: value = node.val : parent
        parents = collections.defaultdict(TreeNode)
        
        def find_parent(node):
            if node.left:
                parents[node.left.val] = node
                find_parent(node.left)
            if node.right:
                parents[node.right.val] = node
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
        
        def dfs(cur, k):
            seen.add(cur)
            if k == 0:
                res.append(cur.val)
                return
            
            if cur.left and cur.left not in seen:
                dfs(cur.left, k - 1)
            
            if cur.right and cur.right not in seen:
                dfs(cur.right, k - 1)
            
            if cur.val in parents and parents[cur.val] not in seen:
                dfs(parents[cur.val], k - 1)
        
        res = []
        seen = set()
        dfs(target, k)
        return res
        
        
        """
        ## S2: DFS + BFS
        
        if not root: return []
        
        # use DFS to build graph
        graph = collections.defaultdict(list)
        
        def dfs(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        
        dfs(root)
        
        # do BFS to find nodes with dist of K
        seen = set()
        q = [target.val]
        seen.add(target.val)
        
        for _ in range(k):
            nxt = []
            for x in q:
                for y in graph[x]:
                    if y not in seen:
                        nxt.append(y)
                        seen.add(y)
            q = nxt
        
        return q
        """
        
        