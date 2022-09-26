class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        i = 0
        
        for j, v in enumerate(nums):
            k -= (1 - v)
            if k < 0:
                k += (1 - nums[i])
                i += 1
        
        return j - i + 1
        