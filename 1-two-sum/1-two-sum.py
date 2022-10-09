class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = collections.defaultdict(int)
        
        for i, x in enumerate(nums):
            k = target - x
            if k in d:
                return [d[k], i]
            d[x] = i
        