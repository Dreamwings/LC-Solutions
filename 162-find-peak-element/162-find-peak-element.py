class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return 0
        l, r = 0, n - 1
        
        # while l < r:
        #     m = (l + r) >> 1
        #     if nums[m] < nums[m+1]:
        #         l = m + 1
        #     else:
        #         r = m
        while l <= r:
            m = (l + r) >> 1
            if m + 1 < n and nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1
        
        return l
        