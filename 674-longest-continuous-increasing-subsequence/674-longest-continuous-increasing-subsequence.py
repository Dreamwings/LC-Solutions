class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[j-1] >= nums[j]:
                i = j
            else:
                res = max(res, j - i + 1)
        return res