class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        ## S1: Topological Sort
        
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        prev_leaves = leaves
        while leaves:
            new_leaves = []
            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            prev_leaves, leaves = leaves, new_leaves

        return prev_leaves