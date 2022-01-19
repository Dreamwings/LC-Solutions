class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ## S1:
        
        # the left most val of the k integers must in arr[:n-k]
        # do binary search
        
        n = len(arr)
        l, r = 0, n - 1 - k  # l, r are both valid index [l, r]
        
        while l <= r:
            m = (l + r) >> 1
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m - 1
        
        return arr[l : l+k]
        