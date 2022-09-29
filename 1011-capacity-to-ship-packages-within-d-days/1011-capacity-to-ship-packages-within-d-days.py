class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        
        def meet(w):
            cnt, s = 1, 0
            
            for x in weights:
                s += x
                if s > w:
                    cnt += 1
                    s = x
            
            return cnt <= days
        
        
        while l <= r:
            m = (l + r) >> 1
            if meet(m):
                r = m - 1
            else:
                l = m + 1
        
        return r + 1
                    