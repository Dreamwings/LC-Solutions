class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        lo, hi = 0, len(arr) - 1
        
        while lo <= hi:
            m = (lo + hi) >> 1
            if arr[m] - (m + 1) < k:
                lo = m + 1
            else:
                hi = m - 1
        
        return lo + k
        
        