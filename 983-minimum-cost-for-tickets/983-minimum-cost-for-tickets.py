class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = days[-1]
        dp = [0] * (n + 1)
        d = set(days)
        
        for i in range(1, n + 1):
            if i not in d:
                dp[i] = dp[i-1]
            else:
                i1, i7, i30 = max(0, i-1), max(0, i-7), max(0, i-30)
                dp[i] = min(dp[i1] + costs[0], dp[i7] + costs[1], dp[i30] + costs[2])
        
        return dp[-1]