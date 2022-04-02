class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        ## S1: DFS Backtracking
        
        q, cols, xy_sum, xy_dif = [], [], [], []
        
        def dfs(q, cols, xy_sum, xy_dif):
            x = len(cols)  # current len of cols actually is the row number to be visited next
            if x == n:
                q.append(cols)
                return
            
            for y in range(n):  # y is the col number to be visited next
                col_good = y not in cols  # this col is not occupied by previous Queens
                pos_good = (x + y) not in xy_sum  # no Queens on positive 45 degree line
                neg_good = (x - y) not in xy_dif  # no Queens on negative 45 degree line
                if col_good and pos_good and neg_good:
                    dfs(q, cols + [y], xy_sum + [x + y], xy_dif + [x - y])
        
        dfs(q, cols, xy_sum, xy_dif)
        
        res = []
        for col in q:
            row = []
            for y in col:
                row.append('.' * y + 'Q' + '.' * (n - 1 - y))
            
            res.append(row)
            
        return res