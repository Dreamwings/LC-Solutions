from sortedcontainers import SortedList
    
class MyCalendar(object):
    
    def __init__(self):
        self.a = SortedList()
        

    def book(self, start, end):
        
        i = SortedList.bisect_right(self.a, start)
        j = SortedList.bisect_left(self.a, end)
        
        if i == j and i % 2 == 0: # i is even
            self.a.add(start)
            self.a.add(end)
            # print(self.a)
            return True
        
        return False
        
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)