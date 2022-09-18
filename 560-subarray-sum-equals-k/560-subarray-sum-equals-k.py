class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from collections import defaultdict
        
        d = defaultdict(int)
        d[0] = 1
        s, res = 0, 0
        
        for x in nums:
            s += x
            if s - k in d:
                res += d[s - k]
            d[s] += 1
        
        return res