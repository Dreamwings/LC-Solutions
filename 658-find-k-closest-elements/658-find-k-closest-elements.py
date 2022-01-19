class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ## S1: Binary Search
        ## Time: O(log(N-K))
        ## Space: O(1)
        ## Modified binary search with [l, r] instead of [l, r)
        
        # since the output has k values, the left most one must be in arr[:n-k]
        # do binary search for this left most output
        n = len(arr)
        l, r = 0, n - 1 - k  # l, r are both valid index [l, r]
        
        while l <= r:
            m = (l + r) >> 1
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m - 1
        
        return arr[l : l+k]
        
        """
        ## Original code with [l, r) Binary Search
        n = len(arr)
        lo, hi = 0, n - k
        
        while lo < hi:
            m = (lo + hi) >> 1
            
            if x - arr[m] > arr[m+k] - x:
            # which is the same as: x > (arr[m] + arr[m+k]) / 2
                lo = m + 1
            else:
                hi = m
        
        ## the following codes explains the above ones
        # while lo < hi:
        #     m = (lo + hi) >> 1
        #     if x <= arr[m]:  # x is on the left of window arr[m : m+k], window move left
        #         hi = m
        #     elif x >= arr[m+k]: # x is on the right of window arr[m : m+k]
        #         lo = m + 1
        #     elif x - arr[m] > arr[m+k] - x:  # x is inside of the window, but on the right
        #         lo = m + 1
        #     else:
        #         hi = m
                        
        return arr[lo : lo + k]
        
        """