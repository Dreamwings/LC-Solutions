# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1: return n
        l, r = 1, n
        
        while l <= r:
            m = (l + r) >> 1
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
                
        return l
        
        """
        if n == 1: return 1
        l, r = 1, n
        
        while l <= r:
            m = (l + r) >> 1
            if isBadVersion(m) == True and isBadVersion(m-1) == False:
                return m
            elif isBadVersion(m) == True:
                r = m - 1
            elif isBadVersion(m) == False:
                l = m + 1
        
        """        
        
        