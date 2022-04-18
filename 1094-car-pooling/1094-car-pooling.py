class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        d = collections.defaultdict(int)
        
        for x, fr, to in trips:
            d[fr] += x
            d[to] -= x
        
        cnt = 0
        for i in sorted(d):
            cnt += d[i]
            if cnt > capacity:
                return False
        return True