class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        
        # yi + yj + |xi - xj| = yi + yj - xi + xj because points is sorted by x and i < j
        # = (yi - xi) + yj + xj
        
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