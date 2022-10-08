class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        from collections import Counter
        
        d = Counter(s)
        zero_left = d['0']  # how many '0' left on the right of the current place
        ones_seen = 0       # how many '1' counted by the current place
        res = d['1']
        
        for c in s:
            if c == '0':
                zero_left -= 1
            else:
                res = min(res, zero_left + ones_seen)
                ones_seen += 1
                
        return res        