class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ## S 1: DFS + BFS
        
        
        # first use DFS to find all cells of one island
        # then apply BFS to all the cells to reach new cells and count the steps
        # when reaching a cell with 1, that's the smallest number of steps
        
        n = len(grid)
        first = set()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y):
            first.add((x, y))
            grid[x][y] = 'X'  # mark as visited
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < n and (i, j) not in first and grid[i][j]:
                    dfs(i, j)
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    found = True
                    dfs(i, j)
                    break
            if found:
                break
        
        # now we have all the cells of first island, let them as starting point to move
        step = 0
        
        while first:
            next_level = []  # can use a set too.
            for x, y in first:
                for dx, dy in d:
                    i, j = x + dx, y + dy
                    if 0 <= i < n and 0 <= j < n:
                        if grid[i][j] == 1:
                            return step
                        elif grid[i][j] == 0:
                            next_level.append((i, j))
                            grid[i][j] = -1  # mark as visited to aviod a visited set
            step += 1
            first = next_level
        
        