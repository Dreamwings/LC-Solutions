class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        g = [[0] * n for _ in range(m)]
        
        def dfs(x, y):
            if not g[x][y]: # (x, y) not visited
                cur_max = 0
                for dx, dy in dir:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and matrix[x][y] < matrix[i][j]:
                        cur_max = max(cur_max, dfs(i, j))
                g[x][y] = 1 + cur_max
            return g[x][y]
        
        res = 0
        for i in range(m):
            for j in range(n):
                g[i][j] = dfs(i, j)
                res = max(res, g[i][j])
                
        return res