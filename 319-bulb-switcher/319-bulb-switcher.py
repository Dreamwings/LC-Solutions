class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        ## S1:
        ## Check how many nums in [1, 2, ..., n] have odd number of factors
        ## 1: 1, [1]
        ## 2: 2, [1, 2]
        ## 3: 2, [1, 3]
        ## 4: 3, [1, 2, 4]
        ## ...
        ## 8: 4, [1, 2, 4, 8]
        ## 9: 3, [1, 3, 9]
        ## only pefect square numbers meet the requirement, 1, 4, 9, 16...
        
        return int(n**0.5)
        
        """
        ##
        ##.    1  2  3  4  5  6  7  8  9 10
        ## R1: 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ## R2: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0
        ## R3: 1, 0, 0, 0, 1, 1, 1, 0, 0, 0
        ## R4: 1, 0, 0, 1, 1, 1, 1, 1, 0, 0
        ## R5: 1, 0, 0, 1, 0, 1, 1, 1, 0, 1
        ## R6: 1, 0, 0, 1, 0, 0, 1, 1, 0, 1
        ## R7: 1, 0, 0, 1, 0, 0, 0, 1, 0, 1
        ## R8: 1, 0, 0, 1, 0, 0, 0, 0, 0, 1
        ## R9: 1, 0, 0, 1, 0, 0, 0, 0, 1, 1
        
        ## if a bulb is toggled odd number of times, it's on
        ## if a bulb is toggled even number of times, it's off
        ## the number of times on a bulb determined by the number of factors of it's index (starting from 1)
        ## a number with odd factors must be a squared number x**2 because: 
        ## for every factor a in range(1, x), it has a pair a * b = x ** 2 where b > x
        ## it also has a factor of x, so the number of factors is odd
        ## so we just need to find how many squared number in range(1, n+1)
        
        ## S2:
        
        from math import sqrt
        
        return int(sqrt(n))
        """
        