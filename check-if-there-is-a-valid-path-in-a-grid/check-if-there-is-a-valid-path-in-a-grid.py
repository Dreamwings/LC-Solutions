class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
        ## S1: DFS
        
        if not grid: return True
        m, n = len(grid), len(grid[0])
        d = {1: [(0, -1), (0, 1)],
             2: [(-1, 0), (1, 0)],
             3: [(0, -1), (1, 0)],
             4: [(0, 1), (1, 0)],
             5: [(-1, 0), (0, -1)],
             6: [(-1, 0), (0, 1)]
             }
        
        seen = set()
        
        def dfs(x, y):
            # print(x, y)
            seen.add((x, y))
            if (x, y) == (m-1, n-1):
                return True
            for dx, dy in d[grid[x][y]]:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and (i, j) not in seen and (-dx, -dy) in d[grid[i][j]]:
                    if dfs(i, j):
                        return True
            return False
        
        return dfs(0, 0)
        