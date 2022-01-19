class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        ## S1: Binary Search
        
        def meet(mid):
            cnt, s = 1, 0
            # note that initilize cnt to 1 so that even s > 0 with the last x, 
            # we don't need to consider cnt specially.
            for x in weights:
                s += x
                if s > mid:
                    cnt += 1
                    s = x
                # note that if s == mid, it will go to next round to increase cnt
            return cnt <= days
        
        l, r = max(weights), sum(weights)
        
        while l <= r:
            m = (l + r) >> 1
            # print(l, r, m, meet(m))
            if meet(m):
                r = m - 1
            else:
                l = m + 1
            
        return l
        
        """
        ## Original codes:
        
        def can_finish(mid):
            s, cnt = 0, 1
            for x in weights:
                if s + x > mid:
                    cnt += 1
                    s = 0
                s += x
            
            return cnt <= days
        
        lo, hi = max(weights), sum(weights)
        
        while lo <= hi:
            m = (lo + hi) >> 1
            if can_finish(m):
                hi = m - 1
            else:
                lo = m + 1
        
        return lo
        """