class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        ## Solution 2: DP
        ## Time: O(N^2)
        ## Space: O(N)
        
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
                # dp[j-1] on the right is (j-1) cell status of the current row, it's already updated
                # dp[j] on the right side is the j-th cell status of the previous row, it has not been updated before this assignment.
        
        return dp[-1]
        
        """
        ## Solution 1: DP
        ## Time: O(N^2)
        ## Space: O(N^2)
        
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
        """
        
        