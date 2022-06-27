class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        ## S2: Heapq
        
        from heapq import nlargest, nsmallest
        
        n = len(nums)
        if n <= 4: return 0
        
        a = nlargest(4, nums)
        a = a[::-1]  # now a is sorted from small to large
        b = nsmallest(4, nums)
        # print(a, b)
        res = float('inf')
        
        for x, y in zip(a, b):
            res = min(res, x - y)
        
        return res