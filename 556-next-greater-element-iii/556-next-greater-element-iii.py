class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        a = [int(x) for x in str(n)]
        m = len(a)
        i = j = m - 1
        
        while i and a[i-1] >= a[i]:
            i -= 1
        
        if i == 0:
            return -1
        
        k = i - 1
        while j and a[j] <= a[k]:
            j -= 1
        
        a[k], a[j] = a[j], a[k]
        
        # now reverse a[i:]
        a[i:] = a[i:][::-1]
        
        res = int(''.join([str(x) for x in a]))
        
        if res <= 2**31 - 1: return res
        else: return -1
        
        