class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        ## S1: Two Pointers
        ## every time move the pointer with a lower bound
        
        n = len(height)
        if n <= 2: return 0
        
        i, j = 0, n - 1
        l, r = height[0], height[n-1]  # max h from left and from right so far
        res = 0
        
        while i < j:
            h = min(l, r)
            if l == h: # when l <= r
                res += max(0, h - height[i])
                i += 1
                l = max(l, height[i])
            else:  # when r == h, l > r
                res += max(0, h - height[j])
                j -= 1
                r = max(r, height[j])
                
        return res