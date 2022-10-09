class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        
        ## https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/446088/Python-DP-with-explaination
        
        
        N = len(stones)
        if (N - 1) % (k - 1): return -1
        prefix = [0] * (N+1)
        for i in range(1,N+1): prefix[i] = stones[i-1] + prefix[i-1]
        dp = [[0] * N for _ in range(N)]
        for m in range(k, N+1):
            for i in range(N-m+1):
                dp[i][i+m-1] = min(dp[i][j] + dp[j+1][i+m-1] for j in range(i, i+m-1, k-1)) + (prefix[i+m] - prefix[i] if (m-1)%(k-1) == 0 else 0)
        return dp[0][N-1]

        