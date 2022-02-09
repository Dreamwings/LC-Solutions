class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        ## S1:
        ## https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2755/9-lines-O(log(min(mn)))-Python
        ## Time: O(logmin(m,n)))
        ## Space: O(1)
        
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)  # m <= n
        mid = (m + n - 1) >> 1
        l, r = 0, m - 1
        
        while l <= r:
            x = (l + r) >> 1
            y = mid - x - 1
            if y < 0 or a[x] >= b[y]:
                r = x - 1
            else:
                l = x + 1
                
        mid_vals = sorted(a[l : l+2] + b[mid-l : mid - l + 2]) # four vals
        # print(l, mid)
        # print(mid_vals)
        if (m + n) & 1:  # odd
            return mid_vals[0]
        else:
            return (mid_vals[0] + mid_vals[1]) / 2.0
        
        """
        ## S2: Find Kth Element of Two Sorted Arrays
        ## https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
        
        def kth(a, b, k):
            # find the (k+1)-th element
            # note that array slicing is O(N), so this is not real O(logN)
            # but can change the array slicing with indices as also shown in the above link
            if not a: return b[k]
            if not b: return a[k]
            i, j = len(a) // 2, len(b) // 2
            ma, mb = a[i], b[j]
            
            if i + j < k: 
                if ma > mb: # a's median larger than b's, b's first half doesn't include k
                    return kth(a, b[j+1:], k - j - 1)
                else:
                    return kth(a[i+1:], b, k - i - 1)
            else:
                if ma > mb: # a's second half doesn't include k
                    return kth(a[:i], b, k)
                else:
                    return kth(a, b[:j], k)
                    
        n = len(nums1) + len(nums2)
        if n & 1:
            return kth(nums1, nums2, n//2)
        else:
            return 0.5 * (kth(nums1, nums2, n//2) + kth(nums1, nums2, n//2 - 1))
        
        """