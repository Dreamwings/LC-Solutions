class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        ## S1: Two Pointers
        ## every time move the pointer with a lower bound
        
        n = len(height)
        if n <= 2: return 0
        i, j = 0, n - 1
        l, r = height[0], height[n-1]
        rain = 0
        
        while i < j:
            h = min(l, r)
            if l == h:  # left side lower
                rain += max(0, h - height[i])
                i += 1
                l = max(l, height[i])
            else:  # right side lower
                rain += max(0, h - height[j])
                j -= 1
                r = max(r, height[j])
                
        return rain