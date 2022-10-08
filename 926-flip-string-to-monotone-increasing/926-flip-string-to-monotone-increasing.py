class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        from collections import Counter
        
        ## S2: Optimization of S1
        
        res = flips = Counter(s)['0']
        # res = flips = s.count('0')
        
        for c in s:
            if c == '1':
                flips += 1
            else:
                flips -= 1
                res = min(res, flips)
        
        return res
        
        """
        ## S1:
        ## https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/184110/python-O(n)-time-O(1)-space-solution-with-explanation(with-extra-Chinese-explanation)
        
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
        """