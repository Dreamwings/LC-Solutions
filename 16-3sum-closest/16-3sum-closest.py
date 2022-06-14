class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ## Solution 1: Two Pointers
        ## Time: O(N^2)
        ## Space: sorting
        
        nums.sort()
        diff = float('inf')
        res = 0
        
        for i, x in enumerate(nums[:-2]):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = x + nums[l] + nums[r]
                if s == target:
                    return s
                
                d = abs(s - target)
                if d < diff:
                    diff = d
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
                
        return res
            