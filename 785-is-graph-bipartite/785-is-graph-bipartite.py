class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        d = {}
        
        def dfs(x):
            for y in graph[x]:
                if y in d:
                    if d[y] == d[x]:
                        return False
                else:
                    d[y] = 1 - d[x]
                    if not dfs(y):
                        return False
            return True
        
        for x in range(len(graph)):
            if x not in d:
                d[x] = 0
                if not dfs(x):
                    return False
        
        return True
        