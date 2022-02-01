class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res = set()
        seen = set()
        
        for x in nums:
            if x - k in seen:
                res.add((x - k, x))
            if x + k in seen:
                res.add((x, x + k))
            seen.add(x)
        
        return len(res)