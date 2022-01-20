class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        ## S1: Binary Search
        ## https://leetcode-cn.com/problems/kth-missing-positive-number/solution/di-k-ge-que-shi-de-zheng-zheng-shu-by-leetcode-sol/
        
        ## by arr[i], there are arr[i] - (i+1) missing numbers
        ## let m = arr[i] - (i+1), there are m missing numbers before arr[i]
        ## so we need to find x to insert at index i, so that x - (i+1) == k
        ## that is x = (i+1) + k
        ## to find x, we need to find the place to insert it
        
        lo, hi = 0, len(arr) - 1
        
        while lo <= hi:
            m = (lo + hi) >> 1
            if arr[m] - (m + 1) < k:
                lo = m + 1
            else:
                hi = m - 1
        
        return lo + k
        # should return this:
        # arr[lo-1] + (k - (arr[lo-1] - (lo -1 + 1)))
        # = arr[lo-1] + k - arr[lo-1] + lo
        # = lo + k
        
        