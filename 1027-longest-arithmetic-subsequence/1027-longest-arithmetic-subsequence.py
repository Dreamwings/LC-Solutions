class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        from collections import defaultdict
        
        ## S1: DP
        
        n = len(nums)
        if n <= 2: return n
        
        f = [dict() for _ in range(n)]
        res = 0
        
        for i, x in enumerate(nums[1:], start=1):
            for j, y in enumerate(nums[:i]):
                d = x - y
                if d not in f[j]:
                    f[i][d] = 2
                else:
                    f[i][d] = 1 + f[j][d]
                res = max(res, f[i][d])
                
        return res
        
        """
        n = len(nums)
        dp = defaultdict(int)
        res = 0
        
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                if (j, d) not in dp:
                    dp[(i, d)] = 2
                else:
                    dp[(i, d)] = 1 + dp[(j, d)]
                    
                res = max(res, dp[(i, d)])
        return res
        """
        