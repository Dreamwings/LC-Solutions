class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dp = [[0] * n for _ in range(m)]
        
        def dfs(x, y):
            if not dp[x][y]:  # (x, y) was not visited
                max_neighbor = 0
                for dx, dy in d:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                        max_neighbor = max(max_neighbor, dfs(i, j))
                dp[x][y] = max_neighbor + 1
            return dp[x][y]
        
        res = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = dfs(i, j)
                res = max(res, dp[i][j])
                
        return res
        
