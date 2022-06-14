class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ## S1:
        ## Need to consider special case:
        ## 1. '+-12'
        ## 2. '0000-42a123'
        ## 3. '  '
        ## 4. '   +0  123'
        
        neg = None
        s = s.strip()
        if not s: return 0
        
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            neg = False
            s = s[1:]
        
        v = 0
        for c in s:
            if not c.isdigit():
                break
            else:
                v = 10 * v + int(c)
        
        if neg: v = -v
        
        MAX, MIN = 2**31 - 1, -2**31
        if v > MAX: return MAX
        if v < MIN: return MIN
        return v
        
        
        """
        
        ## S2:
        
        x = int(*re.findall('^[\+\-]?\d+', s.lstrip()))
        return max(-2 ** 31, min(2 ** 31 - 1, x))
    
        """
        