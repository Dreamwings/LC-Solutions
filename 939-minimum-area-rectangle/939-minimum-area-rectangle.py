class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        s = set([(x, y) for x, y in points])
        res = float('inf')
        
        for i, (x, y) in enumerate(points):
            for (a, b) in points[:i]:
                if a != x and b != y and (a, y) in s and (x, b) in s:
                    area = abs(a - x) * abs(b - y)
                    res = min(res, area)
                    
        if res == float('inf'): return 0
        return res