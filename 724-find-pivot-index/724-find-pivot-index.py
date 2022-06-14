class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        tot = sum(nums)
        pre = 0
        
        for i, x in enumerate(nums):
            if pre * 2 == tot - x:
                return i
            pre += x
            
        return -1