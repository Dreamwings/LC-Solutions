class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        m, n = len(matrix), len(matrix[0])
        g = [[0] * n for _ in range(m)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y):
            if not g[x][y]:  # (x, y) is not visited
                cur_max = 0
                for dx, dy in dir:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                        cur_max = max(cur_max, dfs(i, j))
                g[x][y] = 1 + cur_max
                
            return g[x][y]
        
        res = 1
        for i in range(m):
            for j in range(n):
                g[i][j] = dfs(i, j)
                res = max(res, g[i][j])
                    
        return res