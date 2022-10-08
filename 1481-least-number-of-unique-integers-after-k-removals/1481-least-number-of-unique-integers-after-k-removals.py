class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        from collections import Counter
        from heapq import heappush, heappop
        
        d = Counter(arr)
        hq = []
        
        for key, v in d.items():
            heappush(hq, (v, key))
        
        while k > 0:
            v, _ = heappop(hq)
            k -= v
        
        if k == 0: return len(hq)
        else: return len(hq) + 1
        
        
        