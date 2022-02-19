class TimeMap(object):

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append([timestamp, value])
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.d[key]
        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = (l + r) >> 1
            if arr[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
                
        if r == -1: return ''
        return arr[r][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)