class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        ## S1: Two Pointers
        ## every time move the pointer with a lower bound
        
        n = len(height)
        i, j = 0, n - 1
        l, r = height[0], height[n-1]
        res = 0
        
        while i < j:
            h = min(l, r)
            if l == h:
                res += max(0, h - height[i])
                i += 1
                l = max(height[i], h)
            else:
                res += max(0, h - height[j])
                j -= 1
                r = max(height[j], h)
        
        return res