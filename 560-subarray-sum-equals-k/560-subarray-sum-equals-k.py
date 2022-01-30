class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from collections import defaultdict
        
        ## S1:
        
        d = defaultdict(int) # store the number of each presum value
        d[0] = 1  # IMPORTANT!!! presum == 0 before it starts at 0
        s, res = 0, 0
        
        for x in nums:
            s += x  # s is the cur presume
            if s - k in d:
                res += d[s - k]
            d[s] += 1
            
        return res
        
        """
        pre = defaultdict(int)  # store the number of each presum value
        s, res = 0, 0
        
        for x in nums:
            s += x
            if s == k:
                res += 1
            if s - k in pre:
                res += pre[s - k]
            pre[s] += 1
        
        return res
        
        
        """