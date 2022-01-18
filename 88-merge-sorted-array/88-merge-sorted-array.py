class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        """
        if n == 0: return nums1
        if m == 0: nums1[:] = nums2[:]
        
        i, j, k = m-1, n-1, m+n-1
        
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
        if j >= 0: nums1[:k+1] = nums2[:j+1]
        """
        
        while m > 0 and n > 0:
            # print(nums1)
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            # print(nums1, m, n)
            # note while condition must be m > 0 and n > 0 because we use index m - 1 and n - 1, so m - 1 >= 0, n - 1 >= 0 
            
        if n > 0: nums1[:n] = nums2[:n]