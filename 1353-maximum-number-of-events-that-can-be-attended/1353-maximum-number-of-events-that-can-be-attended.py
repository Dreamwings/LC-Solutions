class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        from heapq import heappush, heappop
        
        hq = []
        events.sort(key=lambda x: x[0]) 
        # this is faster than events.sort() since we only want to sort the first elem
        n, res = len(events), 0
        i, day = 0, 0
        
        while i < n or hq:
            if not hq:
                day = events[i][0]
            
            while i < n and events[i][0] <= day:
                heappush(hq, events[i][1])
                i += 1
            
            heappop(hq) # pop out the event with the earliest end time, means attend it
            res += 1
            day += 1
            
            while hq and hq[0] < day:
                heappop(hq)
            
        return res        
        
