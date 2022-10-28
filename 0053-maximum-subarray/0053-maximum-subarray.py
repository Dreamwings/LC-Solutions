class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## Solution 1:
        
        s, res = 0, nums[0]
        
        for x in nums:
            s = max(x, s + x)
            res = max(res, s)
                
        return res
    
        """
        
        ## Solution 2:
        
        if not nums: return None
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            
        return max(nums)
        
        ## Solution 3:
        
        if not nums: return None
        
        cur_sum = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if cur_sum < 0:
                cur_sum = 0
                
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
        
        
        
        """    
        