class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        seen = set()
        
        def dfs(x, y, prev):
            
            if (x, y) in seen:
                return True
            seen.add((x, y))
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and (i, j) != prev and grid[i][j] == grid[x][y]:
                    if dfs(i, j, (x, y)):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and dfs(i, j, None):
                    return True
                
        return False    
        