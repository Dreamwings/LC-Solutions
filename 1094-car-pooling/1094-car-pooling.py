class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        d = collections.defaultdict(int)
        
        for x, fr, to in trips:
            d[fr] += x
            d[to] -= x
        
        cnt = 0
        
        for k in sorted(d):
            cnt += d[k]
            if cnt > capacity:
                return False
        
        return True