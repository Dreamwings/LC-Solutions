class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
        ## DFS:
        ## Time: O(MN*MN)
        ## Space: O(MN)
        ## Note that here must use a seen = set() to mark visited cells
        
        m, n = len(grid), len(grid[0])
        seen = set()
        
        def dfs(x, y, prev):
            # prev is the prev cell, need to check not visit this cell again
            # if we make sure we don't go back to the prev cell, and we find a cell in seen,
            # there must be a cycle.
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
                
            
            
        