class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        from heapq import nsmallest, heappush, heappop
        
        ## S2:
        hq = []
        
        for x, y in points:
            heappush(hq, (-x*x-y*y, x, y))
            if len(hq) > K:
                heappop(hq)
        
        res = [(x, y) for _, x, y in hq]
        return res
        
        """
        ## S1:
        
        closest = nsmallest(K, [(x*x + y*y, x, y) for x, y in points])
        
        res = [[x, y] for d, x, y in closest]
        
        return res
        """