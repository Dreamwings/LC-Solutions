class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        from heapq import heappush, heappop, heapify
        
        ## Solution 3: Binary Search
        ## https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
        ## Time: O(Nlog(r−l))
        ## Space: O(1)
        
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
        
        
        
            
        """
        ## Solution 1:
        ## Time: best O(k), worst O(N^2 * logN)
        ## Space: O(K)
        res = []
        n = len(matrix)
        
        for i in range(n):
            if len(res) == k and matrix[i][0] > - res[0]:
                break
            for j in range(n):
                heappush(res, -matrix[i][j])
                # print(i, j, res)
                if len(res) > k:
                    heappop(res)
                    if res and -res[0] < matrix[i][j]:
                        break
                
        return -res[0]
        
        
        ## Solution 2:
        ## https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
        ## Time: O(K*logN)
        ## Space: O(N)
        
        n = len(matrix)
        hq = [(matrix[i][0], i, 0) for i in range(n)] # consider first num of each row
        heapify(hq) # min heap
        
        for i in range(k-1): # pop out (k-1) smallest nums
            num, x, y = heappop(hq)
            if y != n - 1:
                heappush(hq, (matrix[x][y+1], x, y+1)) # push one num on the right of the smallest one
            
        res = heappop(hq) # pop out the kth smallest num
        
        return res[0]
        
        """
        
        
        