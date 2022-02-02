class FreqStack(object):
    
    from collections import defaultdict
    
    def __init__(self):
        self.freq = defaultdict(int)
        self.d = defaultdict(list) # freq: values with this freq
        self.maxf = 0 # max freq

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        self.maxf = max(self.maxf, self.freq[val])
        f = self.freq[val]
        self.d[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        x = self.d[self.maxf].pop()
        self.freq[x] -= 1
        if not self.d[self.maxf]: # no more val with the freq of the old self.maxf
            self.maxf -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()