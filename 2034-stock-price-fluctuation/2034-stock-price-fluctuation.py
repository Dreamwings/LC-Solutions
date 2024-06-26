class StockPrice(object):

    def __init__(self):
        self.timestamps = {}
        self.highestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp, price):
        #Keep track of current prices
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)
        
		#For maximum/minimum
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))
        
    def current(self):
        #Just return the highest timestamp in O(1)
        return self.timestamps[self.highestTimestamp]

    def maximum(self):
        currPrice, timestamp = heappop(self.maxHeap)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while -currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.maxHeap)
            
        heappush(self.maxHeap, (currPrice, timestamp))
        return -currPrice

    def minimum(self):
        currPrice, timestamp = heappop(self.minHeap)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.minHeap)
            
        heappush(self.minHeap, (currPrice, timestamp))
        return currPrice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()