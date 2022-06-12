class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        lo, hi = max(weights), sum(weights)
        
        def meet(x):
            cnt, s = 1, 0
            
            for w in weights:
                s += w
                if s > x:
                    cnt += 1
                    s = w
            
            return cnt <= days
        
        while lo <= hi:
            m = (lo + hi) >> 1
            if meet(m):
                hi = m - 1
            else:
                lo = m + 1
                
        return lo