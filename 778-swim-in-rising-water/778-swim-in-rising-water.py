class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        from heapq import heapify, heappush, heappop
        
        
        ## S1: BFS with Heapq
        ## Time: O(N^2*logN)
        
        n = len(grid)
        if n == 1: return grid[0][0]
        
        hq = [(grid[0][0], 0, 0)]
        grid[0][0] = -1
        t = 0
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while hq:
            v, x, y = heappop(hq)
            t = max(t, v)
            
            if x == y == n - 1:
                return t
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < n and grid[i][j] >= 0:
                    heappush(hq, (grid[i][j], i, j))
                    grid[i][j] = -1
                    
        
        
        
        