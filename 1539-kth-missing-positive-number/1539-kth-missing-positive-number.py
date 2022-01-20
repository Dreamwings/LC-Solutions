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
        ## because arr starting count from 1, while i starting from 0
        ## so we just need to find at which place, arr[i] - (i+1) == k
        ## that is the k-th integer is arr[i] = (i + 1) + k
        
        lo, hi = 0, len(arr) - 1
        
        while lo <= hi:
            m = (lo + hi) >> 1
            if arr[m] - (m + 1) < k:
                lo = m + 1
            else:
                hi = m - 1
        
        return lo + k
        