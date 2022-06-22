class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        ## S1: DP
        
        c = [0] + sorted(cuts) + [n]
        m = len(c)
        f = [[float('inf')] * m for _ in range(m)]
        
        for i in range(m-1):
            f[i][i+1] = 0
        
        for i in range(m-1, -1, -1):
            for j in range(i+2, m):
                for k in range(i+1, j):
                    cost = f[i][k] + f[k][j] + c[j] - c[i]
                    f[i][j] = min(f[i][j], cost)
        
        return f[0][-1]