class MedianFinder:
    
    from heapq import heappush, heappop, heappushpop
    
    def __init__(self):
        self.s = [] # max heap to store neg nums
        self.b = [] # min heap to store pos nums        

    def addNum(self, num: int) -> None:
        
        if len(self.s) == len(self.b):
            x = -heappushpop(self.s, -num)
            heappush(self.b, x)
        else:
            x = heappushpop(self.b, num)
            heappush(self.s, -x)

    def findMedian(self) -> float:
        
        if len(self.s) == len(self.b):
            return (self.b[0] - self.s[0]) / 2.0
        else:
            return self.b[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()