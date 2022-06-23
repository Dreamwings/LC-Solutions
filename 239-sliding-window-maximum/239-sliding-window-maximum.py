class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        d = collections.deque()
        res = []
        
        for i, x in enumerate(nums):
            while d and nums[d[-1]] < x:
                d.pop()
            
            d.append(i)
            if i - d[0] == k:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
        
        return res