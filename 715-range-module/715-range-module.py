from bisect import bisect_left as bl, bisect_right as br
    
class RangeModule(object):
    
    def __init__(self):
        self.d = []

    def addRange(self, left, right):
        i, j = bl(self.d, left), br(self.d, right)
        self.d[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left, right):
        i, j = br(self.d, left), bl(self.d, right)
        return i == j and i%2 == 1

    def removeRange(self, left, right):
        i, j = bl(self.d, left), br(self.d, right)
        self.d[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)
                


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)