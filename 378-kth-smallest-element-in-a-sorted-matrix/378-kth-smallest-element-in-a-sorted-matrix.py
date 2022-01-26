class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        
        n = len(matrix)
        
        # define a function to find if the number of element on the left of mid is larger or equal than k
        def check(mid): 
            i, j = n - 1, 0  # starting from matrix[n-1][0]
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    cnt += i + 1 # ***** IMPORTANT!!! *****
                    # all num from matrix[0][j] to matrix[i][j] in column j is not larger than mid
                    j += 1       # can move to the right of the same row
                else:
                    i -= 1       # can move to the up row, but the same column
            # now we got the total number of vals on the left area of the line mid
            return cnt >= k
        
        # now we can use binary search with check function
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):  # on the left of mid it has too many values
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo
            