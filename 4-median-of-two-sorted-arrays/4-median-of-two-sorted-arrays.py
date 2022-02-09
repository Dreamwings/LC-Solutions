class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        ## S1:
        ## https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2755/9-lines-O(log(min(mn)))-Python
        ## Time: O(logmin(m,n)))
        ## Space: O(1)
        
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)  # m <= n
        mid = (m + n - 1) >> 1
        l, r = 0, m - 1
        
        while l <= r:
            i = (l + r) >> 1
            if mid - i - 1 < 0 or a[i] >= b[mid - i - 1]:
                r = i - 1
            else:
                l = i + 1
                
        mid_vals = sorted(a[l : l+2] + b[mid-l : mid - l + 2]) # four vals
        # print(l, mid)
        # print(mid_vals)
        if (m + n) & 1:  # odd
            return mid_vals[0]
        else:
            return (mid_vals[0] + mid_vals[1]) / 2.0
        
        
#         a, b = sorted((nums1, nums2), key=len)
#         m, n = len(a), len(b)
#         after = (m + n - 1) // 2
#         lo, hi = 0, m
#         while lo < hi:
#             i = (lo + hi) // 2
#             if after-i-1 < 0 or a[i] >= b[after-i-1]:
#                 hi = i
#             else:
#                 lo = i + 1
#         i = lo
        
#         nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
#         print(lo, after)
#         print(nextfew)
#         return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
    
    
        ## S2:
        ## https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms