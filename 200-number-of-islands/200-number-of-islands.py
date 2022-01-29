class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ## S1: DFS
        
        m, n = len(grid), len(grid[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y):
            grid[x][y] = '0'
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    dfs(i, j)
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
                    
        return res