class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #     1-9     | 9
        #    10-99    | 90
        #   100-999   | 900 
        #  1000-9999  | 9000 
        # 10000-99999 | 90000
        
        
        digit = base = 1 # starting from 1 digit
        
        while n > 9*base*digit: # upper limit of d digits 
            n -= 9*base*digit
            digit += 1
            base *= 10 
        
        q, r = (n - 1) // digit, (n - 1) % digit
        
        return int(str(base + q)[r])
        
        