class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        m, n = len(board), len(board[0])
        
        def dfs(w, x, y):
            if len(w) == 0:
                return True
            
            tmp, board[x][y] = board[x][y], 0
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and w[0] == board[i][j]:
                    if dfs(w[1:], i, j):
                        return True
            
            board[x][y] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(word[1:], i, j):
                    return True
        
        return False
            
        """
        
        m, n = len(board), len(board[0])
        
        def dfs(word, x, y):
            if len(word) == 0: return True
            if x < 0 or x >= m or y < 0 or y >= n or word[0] != board[x][y]:
                return False
            
            tmp, board[x][y] = board[x][y], '*'  ## Mark visited cell
            
            d1 = dfs(word[1:], x + 1, y)
            d2 = dfs(word[1:], x, y + 1)
            d3 = dfs(word[1:], x - 1, y)
            d4 = dfs(word[1:], x, y - 1)
            
            board[x][y] = tmp
            
            return d1 or d2 or d3 or d4
        
        for i in range(m):
            for j in range(n):
                if dfs(word, i, j):
                    return True
        
        return False
        
        """
        