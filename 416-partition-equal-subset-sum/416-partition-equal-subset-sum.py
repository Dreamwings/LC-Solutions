class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ## S 2: DP
        
        s = sum(nums)
        if s & 1: return False
        s >>= 1
        
        dp = [False] * (s + 1)
        dp[0] = True
        
        for x in nums:
            if dp[s]:
                return True
            for y in range(s, x - 1, -1):
                dp[y] = dp[y] | dp[y - x]
        
        return dp[s]
    
        """
        s = sum(nums)
        if s % 2: return False
        
        s = s // 2
        
        seen = set([0])
        
        for x in nums:
            cur = seen.copy()
            for y in cur:
                z = x + y
                if z == s:
                    return True
                elif z < s:
                    seen.add(z)
        
        return False        
        """
        
        