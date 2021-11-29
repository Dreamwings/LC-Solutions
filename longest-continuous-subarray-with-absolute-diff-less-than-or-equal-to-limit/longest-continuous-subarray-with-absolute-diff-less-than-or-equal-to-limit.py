class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        ## S1: Two heaps
        
        from heapq import heappush, heappop
        
        minq, maxq = [], []
        i = 0
        res = 0
        
        for j, x in enumerate(nums):
            heappush(minq, (x, j))
            heappush(maxq, (-x, j))
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heappop(maxq)
                while minq[0][1] < i:
                    heappop(minq)
            
            res = max(res, j - i + 1)
        
        return res
                    