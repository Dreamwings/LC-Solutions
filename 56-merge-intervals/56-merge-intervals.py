class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        a = sorted(intervals, key=lambda x: x[0]) # use a for short, just for coding purpose
        res = [a[0]]
        
        for x, y in a[1:]:
            a, b = res[-1]
            if x <= b:
                res[-1][1] = max(b, y)
            else:
                res.append([x, y])
        
        return res
        