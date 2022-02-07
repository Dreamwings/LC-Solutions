class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import deque
        
        ## S1: BFS
        ## https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/453652/Manhattan-distance-instead-of-normal-goal-check
        
        
        m, n = len(grid), len(grid[0])
        q = deque()
        q.append((0, 0, k, 0))  # x, y, k, steps
        seen = set()
        seen.add((0, 0, k))
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            x, y, kk, steps = q.popleft()
            if (x, y) == (m-1, n-1):
                return steps
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and kk - grid[i][j] >= 0:
                    curr = (i, j, kk - grid[i][j])
                    if curr not in seen:
                        q.append((i, j, kk - grid[i][j], steps + 1))
                        seen.add(curr)
                
        return -1
        
        """    
        
        ## S2: 
        ## an amazing solution from the reply as the main post will fail for some tests, one is:
        ## [[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0],[0,1],[0,1],[0,1],[0,0],[1,0],[1,0],[0,0]]
        ## 4
        ## https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/453652/Manhattan-distance-instead-of-normal-goal-check
        
        m, n = len(grid), len(grid[0])
        start = m-1, n-1, k
        queue = [(-1, 0, start)]
        seen = {start}
        while queue:
            priority, steps, (i, j, k) = heapq.heappop(queue)
            if k >= i + j - 1:
                return steps + i + j
            for i, j in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if m > i >= 0 <= j < n:
                    state = i, j, k - grid[i][j]
                    if state not in seen and state[2] >= 0:
                        heapq.heappush(queue, (i + j + steps + 1, steps + 1, state))
                        seen.add(state)
        return -1   
        """