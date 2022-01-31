class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ## S1:
        ## Time: O(N)
        
        res = 0
        
        for i in range(1, n+1):
            s = set(str(i))
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                res += 1
                
        return res