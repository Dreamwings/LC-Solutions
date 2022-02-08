class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        d = collections.Counter(arr)
        
        for x in sorted(d, key=abs):
            if d[x] > d[2 * x]:
                return False
            d[2 * x] -= d[x]
        
        return True
    
        
        