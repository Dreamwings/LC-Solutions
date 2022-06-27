class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode.com/problems/longest-string-chain/discuss/1213876/Python-3-solutions-LIS-DP-Top-down-DP-Bottom-up-DP-Clean-and-Concise
        ## Time: O(NlogN + N*L*L)
        ## Space: O(N)
        
        words.sort(key=len)
        dp = collections.defaultdict(int)
        res = 0
        
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                pre = w[:i] + w[i+1:]
                if pre in dp:
                    dp[w] = max(dp[w], dp[pre] + 1)
                    
            res = max(res, dp[w])
        return res
        