class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ## S2: Monotone Queue
        ## Time: O(N)
        ## Space: O(K)
        
        from collections import deque
        
        d = deque()
        res = []
        
        for i, x in enumerate(nums):
            while d and nums[d[-1]] < x:
                d.pop()
            d.append(i)
            if i - d[0] == k:  # moving window covers (k+1) elements
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
                
        return res
        
        """
        ## S1: 
        ## https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/
        ## Time: O(N*logN)
        ## Space: O(N)
        
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans

        """