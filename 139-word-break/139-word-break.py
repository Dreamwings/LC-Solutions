class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        ## Solution 1: DP
        
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            for j in range(i+1):
                if dp[j] and s[j : i+1] in words:
                    dp[i+1] = True
                    
        return dp[-1]