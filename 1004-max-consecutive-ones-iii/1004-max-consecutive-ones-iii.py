class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        i = 0
        
        for j, x in enumerate(nums):
            k -= (1 - x)
            if k < 0:
                k += (1 - nums[i])
                i += 1
        
        return j - i + 1
        