class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        # arr = sorted(intervals, key=lambda x: x[0]) # use arr for short, just for coding purpose
        arr = sorted(intervals)
        res = [arr[0]]
        
        for x, y in arr[1:]:
            a, b = res[-1]
            if x <= b:
                res[-1][1] = max(b, y)
            else:
                res.append([x, y])
        
        return res
        