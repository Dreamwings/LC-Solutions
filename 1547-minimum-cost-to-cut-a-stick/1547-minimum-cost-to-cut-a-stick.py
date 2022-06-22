class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        ## S1: DP
        
        c = [0] + sorted(cuts) + [n]
        m = len(c)
        dp = [[float('inf')] * m for _ in range(m)]
        
        for i in range(m-1):
            dp[i][i+1] = 0
        
        for i in range(m-1, -1, -1):
            for j in range(i+2, m):
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + c[j] - c[i]
                    dp[i][j] = min(dp[i][j], cost)
        # print(dp)
        return dp[0][-1]