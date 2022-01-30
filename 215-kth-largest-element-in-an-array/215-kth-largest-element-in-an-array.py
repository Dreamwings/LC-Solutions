class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import nlargest, heappush, heappop
        
        
        ## Solution 1:
        
        return nlargest(k, nums)[-1]
        """
        
        ## Solution 2:
        # O(nlogk)
        
        q = []
        
        for x in nums:  
            heappush(q, x)
            if len(q) > k:
                heappop(q)
        # print(q)
        return q[0]
        
        """