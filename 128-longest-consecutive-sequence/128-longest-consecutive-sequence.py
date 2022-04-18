class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        res = 0
        
        for x in nums:
            if x - 1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                res = max(res, y - x)
        
        return res