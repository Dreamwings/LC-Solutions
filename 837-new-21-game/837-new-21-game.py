class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        
        ## S1: DP
        ## https://leetcode.com/problems/new-21-game/discuss/132334/One-Pass-DP-O(N)
        
        # dp[i] is the probability Alice gets i points at one moment.
        # with moving windows, the game ends when the point is between k and k - 1 + maxPts
        
        if k == 0 or k - 1 + maxPts <= n:
            return 1.0
        
        dp = [1.0] + [0] * n
        s = 1.0
        
        for i in range(1, n+1):
            dp[i] = s / maxPts
            if i < k: # Alice will continue to draw numbers and get points
                s += dp[i]
            if i >= maxPts: # the moving window needs to move the left edge
                s -= dp[i - maxPts]
        
        return sum(dp[k:])