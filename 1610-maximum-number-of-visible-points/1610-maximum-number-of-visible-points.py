class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        ## S1: Sliding Windows
        arr, extra, res = [], 0, 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            xy_angle = math.atan2(y - yy, x - xx)
            arr.append(xy_angle)
        
        arr.sort()
        arr = arr + [x + 2 * math.pi for x in arr]
        angle = angle * pi / 180
        i = 0  # left point of sliding window
        
        for j in range(len(arr)):
            while arr[j] - arr[i] > angle:
                i += 1
            res = max(res, j - i + 1)
            
        return res + extra