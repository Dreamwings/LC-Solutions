class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## S1: Sort
        ## Time: O(NlogN)
        ## Space: O(N)
        
        nums.sort()
        res = 0
        i, j = 0, len(nums) - 1
        
        while i < j:
            res = max(res, nums[i] + nums[j])
            i += 1
            j -= 1
            
        return res
        