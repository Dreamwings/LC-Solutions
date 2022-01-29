class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        
        def smoother(i, j):
            # find the neighbors of (i, j) and sum the vals
            s, cnt = 0, 0
            for x in (i-1, i, i+1):
                for y in (j-1, j, j+1):
                    if 0 <= x < m and 0 <= y < n:
                        cnt += 1
                        s += img[x][y]
            return s // cnt
        
        for i in range(m):
            for j in range(n):
                res[i][j] = smoother(i, j)
        
        return res