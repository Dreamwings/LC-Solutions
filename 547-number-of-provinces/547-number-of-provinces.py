class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        
        def dfs(i):
            for j, v in enumerate(isConnected[i]):
                if v and (j not in visited):
                    visited.add(j)
                    dfs(j)
        
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
            
        return res
        