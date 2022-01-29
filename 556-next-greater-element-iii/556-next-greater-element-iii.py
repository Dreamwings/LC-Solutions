class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ## Ex: 123554321
        ## ==> 124553321
        ## ==> 124123355
        
        a = [int(x) for x in str(n)]
        m = len(a)
        if m == 1: return -1
        i = j = m - 1
        
        while i and a[i-1] >= a[i]:
            i -= 1
        # consider case: 54321
        if i == 0: return -1
        
        k = i - 1
        while j and a[j] <= a[k]:
            j -= 1
        
        a[k], a[j] = a[j], a[k]
        a[i:] = a[i:][::-1] # reverse subarray a[k+1:], note i = k + 1
        
        res = int(''.join([str(x) for x in a]))
        if res <= 2**31 - 1: return res
        return -1
        
        