class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        ## S1: Binary Search
        
        
        def meet(mid):
            s, cnt = 0, 1
            for x in nums:
                if s + x > mid:
                    cnt += 1
                    s = 0
                s += x
            
            return cnt <= m
        
        l, r = max(nums), sum(nums)
        
        while l <= r:
            mid = (l + r) >> 1
            # print(l, r, mid, meet(mid))
            if meet(mid):
                r = mid - 1
            else:
                l = mid + 1
            
        return l
        