class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        
        def check(mid):
            i, j = n - 1, 0
            cnt = 0
            
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    cnt += (i + 1)      # IMPORTANT!!!
                    j += 1
                else:
                    i -= 1
            
            return cnt >= k
        
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l <= r:
            m = (l + r) >> 1
            # print(l, r, m, check(m))
            if check(m):
                r = m - 1
            else:
                l = m + 1
        
        return l
        
        
        
        