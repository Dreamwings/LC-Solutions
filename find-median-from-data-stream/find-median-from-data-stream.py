class MedianFinder:
    
    from heapq import heappush, heappop, heappushpop
    
    def __init__(self):
        self.lo = [] # max heap to store neg nums
        self.hi = [] # min heap to store pos nums        

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            t = -heappushpop(self.lo, -num)
            heappush(self.hi, t)
        else:
            t = heappushpop(self.hi, num)
            heappush(self.lo, -t)

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2.0
        else:
            return self.hi[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()