class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        a = [int(x) for x in str(n)]
        m = len(a)
        i = j = m - 1
        
        # find the first place a[i-1] < a[i] from right most
        while i and a[i-1] >= a[i]:
            i -= 1
        # consider case: 54321
        if i == 0: 
            return -1
        
        # find the place to switch with a[i-1]
        k = i - 1
        
        while j and a[j] <= a[k]:
            j -= 1
        
        # now swap the digit at k and j
        a[k], a[j] = a[j], a[k]
        # print(a)
        # now need to reverse a[i:]
        a[i:] = a[i:][::-1]
        a = [str(x) for x in a]
        res = int(''.join(a))
        
        if res <= 2**31 - 1: return res
        else: return -1
        