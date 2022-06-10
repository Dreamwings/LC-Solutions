class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import Counter
        
        m, n = len(s), len(t)
        if m < n or n == 0:
            return ''
        d = Counter(t)
        l, r, i = 0, float('inf'), 0
        
        for j, c in enumerate(s):
            d[c] -= 1
            if d[c] >= 0:
                n -= 1
            
            if n == 0:
                while i < j and d[s[i]] < 0:
                    d[s[i]] += 1
                    i += 1
                if j - i < r - l:
                    l, r = i, j
        
        if r == float('inf'): return ''
        return s[l : r+1]