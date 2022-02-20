class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        
        ## S1: DP
        
        from collections import defaultdict
        
        dp = defaultdict(int)
        
        for x in arr:
            dp[x] = max(dp[x], dp[x - difference] + 1)
            
        
        return max(dp.values())
        """
        
        ## S2:
        
        d = {}
        
        for x in arr:
            # print(d.items())
            d[x] = 1 + d.get(x - difference, 0)
            
        return max(d.values())
        """