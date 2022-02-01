class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = j = n - 1
        
        while i and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        k = i - 1
        while nums[k] >= nums[j]:
            j -= 1
            
        nums[k], nums[j] = nums[j], nums[k]
        
        nums[i:] = nums[i:][::-1]
        
        