class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m, n = len(board), len(board[0])
        a, b = click
        
        def dfs(x, y):
            d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            mines = 0
            
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'M':
                    mines += 1
            
            if mines == 0:
                board[x][y] = 'B'
            else:
                board[x][y] = str(mines)
                return
            
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'E':
                    dfs(i, j)
        
        if board[a][b] == 'M':
            board[a][b] = 'X'
            return board
        
        dfs(a, b)
        return board
        