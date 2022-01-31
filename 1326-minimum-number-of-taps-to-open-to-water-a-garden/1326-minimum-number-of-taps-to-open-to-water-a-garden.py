class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        
        ## S1: Greedy
        ## https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484272/Python-O(1)-memory-O(n)-time-Greedy-With-Explanation-(132ms-beats-100)
        ## Time: O(N)
        ## Space: O(1)
        
        # modify ranges in place so that each element represents the furthest index you can reach by taking one jump.
        for i, x in enumerate(ranges):
            l = max(0, i - x)
            r = min(n, i + x)
            ranges[l] = max(ranges[l], r)
        
        # Find the minimal jump you need to reach the end index n
        lo = hi = 0
        res = 0
        while hi < n:
            lo, hi = hi, max(ranges[lo : hi+1])
            if hi == lo:  # can't move to the right
                return -1
            res += 1
        
        return res