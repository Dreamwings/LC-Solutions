class Solution:
    def numSplits(self, s: str) -> int:
        
        from collections import Counter
        
        l, r = Counter(), Counter(s)
        res = 0
        
        for c in s:
            l[c] += 1
            r[c] -= 1
            
            if r[c] == 0:
                del r[c]
            
            if len(l) == len(r):
                res += 1
        
        return res