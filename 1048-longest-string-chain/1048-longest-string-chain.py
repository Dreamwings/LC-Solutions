class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        ## S1: DP
        
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