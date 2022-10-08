class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        from collections import Counter
        from heapq import heapify, heappop
        
        d = Counter(arr)
        hq = list(d.values())
        heapify(hq)
        
        while k > 0:
            v = heappop(hq)
            k -= v
        
        if k == 0: return len(hq)
        else: return len(hq) + 1
        
        
        