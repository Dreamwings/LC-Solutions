class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        q.append((0, 0, k, 0))
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