class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## S1: Set
        ## Time: O(N)
        ## Space: O(N)
        
        s = set(nums)
        res = 0
        
        for x in nums:
            if x - 1 not in s:
                # x is the starting point of the sequence
                y = x + 1
                while y in s:
                    y += 1
                res = max(res, y - x)
        return res