class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        ## S1:
        
        cnt, res = 0, 0
        
        for c in s:
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                res += 1
                cnt = 0
                
        return res + cnt
        
        
        """
        ## S2: 
        missing_l, missing_r = 0, 0
        
        for c in s:
            if c == '(':
                missing_r += 1
            elif c == ')':
                if missing_r > 0:
                    missing_r -= 1
                else:
                    missing_l += 1
        
        return missing_l + missing_r
        
        """