class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        ## S2:
        
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i + j].append(mat[i][j]) 
        
        res = []
        for k, v in d.items():
            if k & 1 == 0:  # k even
                res += v[::-1]
            else:
                res += v
        
        return res
        
        """
        ## S1
        
        m, n = len(mat), len(mat[0])
        res = []
        f = 0
        i, j = 0, 0
        
        while len(res) < m * n:
            res.append(mat[i][j])
            if f == 0:
                if j == n - 1:
                    f = 1
                    i += 1
                elif i == 0:
                    f = 1
                    j += 1
                else:
                    i, j = i - 1, j + 1
            else:
                if i == m - 1:
                    f = 0
                    j += 1
                elif j == 0:
                    f = 0
                    i += 1
                else:
                    i, j = i + 1, j - 1
        
        return res            
        """
        