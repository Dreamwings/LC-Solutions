class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        ## [1,2,4,4,3,3,0,9,2,3], k = 3
        ## in the example, (3, 0) and (0, 3) are the same k-diff pairs
        
        res = set()
        seen = set()
        
        for x in nums:
            if x - k in seen:
                res.add((x - k, x))
            if x + k in seen:
                res.add((x, x + k))  # note here always keep smaller one in front
            seen.add(x)
        
        return len(res)