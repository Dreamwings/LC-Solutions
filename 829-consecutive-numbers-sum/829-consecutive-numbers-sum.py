class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ## S1:
        
        # n = k + (k + 1) + ... + (k + i - 1)
        # n = k * i + i * (i - 1) / 2
        # n - i * (i - 1) / 2 = k * i
        
        res = 0
        i = 1
        
        while n > i * (i - 1) // 2:
            if (n - i * (i - 1) // 2) % i == 0:
                res += 1
            i += 1
        
        return res
