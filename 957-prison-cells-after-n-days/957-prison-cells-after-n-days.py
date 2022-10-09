class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        
        n = (n - 1) % 14 + 1
        # after 14 operations, it start to repeat from the result of the 1st operation
        # but we must make the 1st operation, that's why we must use (n - 1)
        
        for k in range(n):
            new = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    new[i] = 1
            cells = new
            # print(k, cells)
        
        return cells        
        