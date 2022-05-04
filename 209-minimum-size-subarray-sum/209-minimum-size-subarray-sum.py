class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ## S2: Two Pointers
        
        i = s = 0
        n = len(nums)
        res = n + 1
        
        for j in range(n):
            s += nums[j]
            while s >= target:
                res = min(res, j - i + 1)
                s -= nums[i]
                i += 1
        
        if res == n + 1: return 0
        return res