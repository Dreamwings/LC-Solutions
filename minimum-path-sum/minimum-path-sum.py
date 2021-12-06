class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        """
        m, n = len(grid), len(grid[0])
        dp = [x for x in grid[0]]
        for i in range(1, n):
            dp[i] += dp[i-1]
        
        for i in range(1, m):
            for j in range(n):
                dp[j] = grid[i][j] + min(dp[j-1], dp[j])
            
        return dp[-1]
        """
        
        ## S2:
        
        m, n = len(grid), len(grid[0])
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]