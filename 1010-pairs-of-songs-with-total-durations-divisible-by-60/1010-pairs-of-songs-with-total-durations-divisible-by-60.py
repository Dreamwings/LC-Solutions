class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        from collections import Counter
        
        d = Counter()
        res = 0
        
        for x in time:
            d[x % 60] += 1
        
        for k in range(1, 30):
            res += d[k] * d[60 - k]
        
        # consider d[0] and d[30]
        res += d[0] * (d[0] - 1) // 2 + d[30] * (d[30] - 1) // 2
        
        return res