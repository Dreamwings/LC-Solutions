class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ## S2: math
        
        from math import ceil
        
        # say need at least M moves for n floor:
        # M + (M-1) + (M-2) + ... + 1 >= n:
        # M*(M+1)//2 >= n
        
        return int(ceil((2 * n + 0.25)**0.5 - 0.5))
        
        """
        ## S1: DP (TLE)
        ## https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/discuss/1246338/Python-DP
        
        def dp(k, n):
            # k is num of eggs left
            if k == 1: return n  # only 1 egg, need to verify floor by floor from bottom
            if n <= 1: return n  # no need to verify
            res = float('inf')
            for f in range(1, n+1):
                res = min(res, 1 + max(dp(k-1, f-1), dp(k, n-f)))
            
            return res
        
        return dp(2, n)
        """
        
        
        
        