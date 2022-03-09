class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        
        ## Solution 1: 
        from bisect import bisect_left, bisect_right
        
        n = len(nums)
        if n == 0: return [-1, -1]
        if target < nums[0] or target > nums[-1]: return [-1, -1]
        
        i = bisect_left(nums, target)
        if nums[i] != target: return [-1, -1]
        
        j = bisect_right(nums, target)
        
        return [i, j-1]
        
        """
        
        ## Solution 2:
        
        n = len(nums)
        if n == 0: return [-1, -1]
        i, j = 0, n - 1
        
        while i < j:
            m = (i + j) >> 1
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        
        if nums[i] != target: return [-1, -1]
        lo = i
        
        i, j = lo, n - 1
        while i < j:
            m = 1 + (i + j) >> 1
            if nums[m] == target:
                i = m
            else:
                j = m - 1
        
        hi = i
        return [lo, hi]
        
        """
        
        