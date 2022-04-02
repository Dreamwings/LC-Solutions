class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        q, cols, xy_sum, xy_dif = [], [], [], []
        
        def dfs(q, cols, xy_sum, xy_dif):
            x = len(cols)
            if x == n:
                q.append(cols)
                return
        
            for y in range(n):
                s, d = x + y, x - y
                col_good = y not in cols
                pos_good = s not in xy_sum
                neg_good = d not in xy_dif
                if col_good and pos_good and neg_good:
                    dfs(q, cols + [y], xy_sum + [s], xy_dif + [d])
        
        dfs(q, cols, xy_sum, xy_dif)
        res = []
        
        for col in q:
            row = []
            for y in col:
                row.append('.' * y + 'Q' + '.' * (n-1-y))
            res.append(row)
            
        return res