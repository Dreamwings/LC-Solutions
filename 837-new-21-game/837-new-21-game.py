class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        if k == 0 or k - 1 + maxPts <= n:
            return 1.0
        
        dp = [1.0] + [0] * n
        s = 1.0
        
        for i in range(1, n+1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            
            if i >= maxPts:
                s -= dp[i - maxPts]
        
        return sum(dp[k:])