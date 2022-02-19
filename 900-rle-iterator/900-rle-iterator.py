class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.a = encoding
        self.i = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        while n > 0 and self.i < len(self.a):
            if n > self.a[self.i]:
                n -= self.a[self.i]
                self.i += 2
            else:
                self.a[self.i] -= n
                return self.a[self.i + 1]
            
        return -1 


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)