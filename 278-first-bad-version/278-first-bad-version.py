# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if n == 1: return n
        l, r = 1, n
        
        while l <= r:
            m = (l + r) >> 1
            # print(l, r, m, isBadVersion(m))
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
                
        return l