class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        self.g = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                self.g[i+1][j+1] = matrix[i][j] + self.g[i+1][j] + self.g[i][j+1] - self.g[i][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        r1, c1 = row1, col1
        r2, c2 = row2 + 1, col2 + 1
        
        return self.g[r2][c2] - self.g[r2][c1] - self.g[r1][c2] + self.g[r1][c1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)