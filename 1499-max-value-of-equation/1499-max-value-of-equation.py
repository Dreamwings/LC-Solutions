class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        # yi + yj + |xi - xj| = yi + yj - xi + xj because points is sorted by x and i < j
        # = (yi - xi) + yj + xj
        
        ## S2: Mono Queue
        ## Time: O(N)
        ## Space: O(N)
        
        q = collections.deque()
        res = float('-inf')
        
        for x, y in points:
            while q and x - q[0][0] > k:
                q.popleft()
            
            if q:
                res = max(res, q[0][1] - q[0][0] + x + y)
            
            while q and q[-1][1] - q[-1][0] < y - x:
                q.pop()
            
            q.append((x, y))
            
        return res
    
        """
        
        ## S1: Priority Queue
        ## Time: O(NlogN)
        ## Space: O(N)
        ## yi + yj + |xi - xj| = yi - xi + yj + xj because points is sorted
        ## to get max (yi - xi), use a max heap with -(yi - xi) = (xi - yi)
        
        from heapq import heappush, heappop
        
        hq = []  # store (xi - yi, xi)
        res = float('-inf')
        
        for x, y in points:
            while hq and x - hq[0][1] > k:
                heappop(hq)
            if hq:
                res = max(res, -hq[0][0] + x + y)
            heappush(hq, (x - y, x))
        
        return res
        """