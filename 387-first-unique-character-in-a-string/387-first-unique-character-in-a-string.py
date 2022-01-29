class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        from collections import defaultdict, Counter
        
        
        ## S2:
        
        d = Counter(s)
        res = -1
        
        for i, c in enumerate(s):
            if d[c] == 1:
                res = i
                break
                
        return res
        
        """
        ## S1: faster
        
        d, seen = defaultdict(int), set()
        
        for i, c in enumerate(s):
            if c not in seen:
                d[c] = i
                seen.add(c)
            elif c in d:
                del d[c]
        
        if not d: return -1
        return min(d.values())
        
        
        """
        
        
        