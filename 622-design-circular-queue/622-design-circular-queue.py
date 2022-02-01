class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [-1]*k
        self.k, self.front, self.end = k, 0, 0
        
    def enQueue(self, value):
        if self.isFull(): return False
        self.end -= 1
        self.q[self.end % self.k] = value
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        self.front -= 1
        self.q[self.front % self.k] = -1
        return True

    def Front(self):
        if self.isEmpty(): return -1
        return self.q[(self.front - 1) % self.k]     

    def Rear(self):
        if self.isEmpty(): return -1
        return self.q[self.end % self.k]      

    def isEmpty(self):
        return self.front == self.end
        
    def isFull(self):
        return self.front - self.end == self.k        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()