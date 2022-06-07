class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        M = days[-1]  # last day, also the largest num in days
        dp = [0] * (M + 1)
        
        # for each day from day 1 to day M, check if it's in days
        # if not, its dp[i] = dp[i-1]
        # else it's the min of the 3 pass choices
        days = set(days)
        
        for i in range(1, M+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                i1, i7, i30 = max(0, i - 1), max(0, i - 7), max(0, i - 30)
                dp[i] = min(dp[i1] + costs[0],  dp[i7] + costs[1], dp[i30] + costs[2])
                
        return dp[-1]
        