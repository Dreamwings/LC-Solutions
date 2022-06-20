class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
        ## S1:
        
        m, n = len(nums1), len(nums2)
        if m > n:
            a, b = nums2, nums1
            m, n = n, m
        else:
            a, b = nums1, nums2
        
        mid = (m + n - 1) // 2
        lo, hi = 0, m
        # print('a:', a)
        # print('b:', b)
        # print('m, n, mid, lo, hi:', m, n, mid, lo, hi)
        
        while lo < hi:
            i = (lo + hi) >> 1
            j = mid - i - 1
            # print('lo, hi, i, j:', lo, hi, i, j)
            if j < 0 or a[i] >= b[j]:
                hi = i
            else:
                lo = i + 1
        
        arr = sorted(a[lo : lo+2] + b[mid-lo : mid-lo+2])
        # print('lo, mid-lo:', lo, mid-lo)
        # print(arr)
        if (m + n) & 1:
            return arr[0]
        else:
            return (arr[0] + arr[1]) / 2.0
        """
        
        ## S2:
        
        def find_kth(a, b, k):
            if not a: return b[k]
            if not b: return a[k]
            
            i, j = len(a) // 2, len(b) // 2
            ma, mb = a[i], b[j]
            
            if i + j < k:
                if ma > mb:
                    return find_kth(a, b[j+1:], k - (j + 1))
                else:
                    return find_kth(a[i+1:], b, k - (i + 1))
            else:
                if ma > mb:
                    return find_kth(a[:i], b, k)
                else:
                    return find_kth(a, b[:j], k)
            
        n = len(nums1) + len(nums2)
        if n & 1:
            return find_kth(nums1, nums2, n // 2)
        else:
            return (find_kth(nums1, nums2, n // 2 - 1) + find_kth(nums1, nums2, n // 2)) * 0.5
            
            
            
            
            
            
            
        