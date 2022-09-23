class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        neg = (dividend < 0) ^ (divisor < 0)
        dd, dr = abs(dividend), abs(divisor)
        res, x = 0, dr
        
        while x <= dd:
            q = 1
            while (x << 1) <= dd:
                x <<= 1
                q <<= 1
            
            res += q
            dd -= x
            x = dr
        
        if neg: res = -res
        M = 2**31
        if res > M - 1: return M - 1
        if res < -M: return -M
        
        return res