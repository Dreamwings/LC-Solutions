class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode-cn.com/problems/maximum-number-of-points-with-cost/solution/kou-fen-hou-de-zui-da-de-fen-by-leetcode-60zl/
        ## Time: O(MN)
        ## Space: O(N)
        
        m, n = len(points), len(points[0])
        f = [0] * n
        
        for i in range(m):
            g = [0] * n
            # from left to right:
            best = float('-inf')
            for j in range(n):
                best = max(best, f[j] + j)
                g[j] = max(g[j], best + points[i][j] - j)
                
            # from right to left
            best = float('-inf')
            for j in range(n-1, -1, -1):
                best = max(best, f[j] - j)
                g[j] = max(g[j], best + points[i][j] + j)
            
            f = g
                
        return max(f)
        