class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ## S1: 
        
        m, n = len(grid), len(grid[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        
        def sum_adj(x, y):
            # check if the four neighbors of (x, y) are 0's or grid boundry
            # if 0, it's an edge, add 1
            cur = 0
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if i < 0 or j < 0 or i == m or j == n or grid[i][j] == 0:
                    cur += 1
            return cur
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += sum_adj(i, j)
        return res
        
        
        """
        
        ## S2: DFS
        
        def dfs(x, y):
            res = 0
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            grid[x][y] = 2
            # any of the below two condition can happen at the same time
            # so must not use 'elif'
            if x == 0:
                res += 1
            if x == m-1:
                res += 1
            if y == 0:
                res += 1
            if y == n-1:
                res += 1
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 0:
                        res += 1
                    elif grid[i][j] == 1:
                        res += dfs(i, j)
            return res
        
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = dfs(i, j)
                    return res
                    
        """
        