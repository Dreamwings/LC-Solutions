class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        ## S1: Binary Search
        ## Time: O(NlogW)
        
        def meet(x):
            cnt = 0
            for v in piles:
                cnt += 1 + (v - 1) // x
            return cnt <= h
        
        l, r = 1, max(piles)
        
        while l <= r:
            m = (l + r) >> 1
            if meet(m):
                r = m - 1
            else:
                l = m + 1
        return l