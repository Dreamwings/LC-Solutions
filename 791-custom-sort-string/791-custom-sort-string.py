class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        d = collections.Counter(s)
        res = ''
        
        for c in order:
            if c in d:
                res += c * d[c]
                del d[c]
        
        for k, v in d.items():
            res += k * v
        
        return res