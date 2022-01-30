class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque
        
        d = deque()
        res = []
        
        for i, x in enumerate(nums):
            while d and nums[d[-1]] < x:
                d.pop()
            
            d.append(i)
            if d[0] + k == i:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
                
        return res