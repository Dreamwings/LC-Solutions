class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        m, n = len(board), len(board[0])
        a, b = click
        
        if board[a][b] == 'M':
            board[a][b] = 'X'
            return board
        
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
                # need to return here because when it's a digit cell, will not move onto it to check its neighbors.
            
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'E':
                    dfs(i, j)
        
        dfs(a, b)
        return board
        