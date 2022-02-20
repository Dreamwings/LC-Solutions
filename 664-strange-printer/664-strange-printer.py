class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode.com/problems/strange-printer/discuss/106795/Python-Straightforward-DP-with-Explanation
        
        # shorten the original string, like reduce aaabbb to ab.
        # this is not neccessary, but it makes DP more efficient
        S = ''
        for a, b in zip(s, '#' + s):
            if a != b:
                S += a
        
        mem = {}
        
        def dp(i, j):
            # Let dp(i, j) be the number of turns needed to print S[i:j+1].
            if i > j: return 0
            if (i, j) in mem:
                return mem[(i, j)]
            cost = dp(i+1, j) + 1
            for k in range(i+1, j+1):
                if S[k] == S[i]:
                    cost = min(cost, dp(i, k-1) + dp(k+1, j))
            mem[(i, j)] = cost
            return mem[(i, j)]
        
        return dp(0, len(S)-1)