class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        ## Solution 1: DFS
        color = {}
        
        def dfs(u):
            for v in graph[u]:
                if v in color:
                    if color[v] == color[u]:
                        return False
                else:
                    color[v] = 1 - color[u]
                    if not dfs(v):
                        return False
            return True
        
        for x in range(len(graph)):
            if x not in color:
                color[x] = 0
                if not dfs(x):
                    return False
                        
        return True
        
        ## Solution 2: BFS
        
        
        
        
        