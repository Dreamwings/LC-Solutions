class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        ## S1:
        ## https://leetcode-cn.com/problems/minimum-area-rectangle/solution/zui-xiao-mian-ji-ju-xing-by-leetcode/
        ## Time: O(N^2)
        
        # find the two points of the diagonal 
        
        s = set([(x, y) for x, y in points])
        res = float('inf')
        
        for i, (a, b) in enumerate(points):
            for (x, y) in points[:i]:
                if a != x and b != y and (a, y) in s and (x, b) in s:
                    # a rectangle exists
                    area = abs(a - x) * abs(b - y)
                    res = min(res, area)
        
        if res == float('inf'): return 0
        return res
        