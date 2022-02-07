class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # remove 3 vals from left/right with sorted arr
        # consider different cases and get their own min diff
        n = len(nums)
        if n <= 4: return 0 # can always remove 3 largest/smallest vals
        
        nums.sort()
        d1 = nums[-4] - nums[0]  # remove 3 largests
        d2 = nums[-3] - nums[1]  # remove 2 largests and 1 smallest
        d3 = nums[-2] - nums[2]  # remove 1 largests and 2 smallest
        d4 = nums[-1] - nums[3]  # remove 3 smallests
        
        return min(d1, d2, d3, d4)