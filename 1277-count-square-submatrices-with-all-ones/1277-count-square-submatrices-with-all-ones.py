class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
        ## Time: O(MN)
        ## Space: O(1)
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] and i > 0 and j > 0:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                res += matrix[i][j]
                    
        return res