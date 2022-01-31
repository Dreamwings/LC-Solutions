class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.d = [0] * k
        self.k = k
        self.i = 0
        self.head = 0  # the starting place with a value
        self.tail = 0  # the first empty place after the last value
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.i == self.k: # full
            return False
        self.head = (self.head - 1) % self.k
        self.d[self.head] = value
        self.i += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.i == self.k:
            return False
        self.d[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.i += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.i == 0:
            return False
        self.head = (self.head + 1) % self.k
        self.i -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.i == 0:
            return False
        self.tail = (self.tail - 1) % self.k
        self.i -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.i == 0: return -1
        return self.d[self.head]

    def getRear(self):
        """
        :rtype: int
        """
        if self.i == 0: return -1
        return self.d[self.tail - 1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.i == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.i == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()