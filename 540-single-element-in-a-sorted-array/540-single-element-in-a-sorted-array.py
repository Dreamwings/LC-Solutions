class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## S2:
        ## Time: O(log(N/2))
        
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            # print(l, r)
            m = (l + r) >> 1
            
            if m - 1 >= 0 and m + 1 < n and nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            
            if m & 1:  # m odd, there are even nums in [0, m]
                m -= 1  # change m to even
            # now m is always even, [0, m] has odd numbers
            if m + 1 < n and nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m - 1
        
        return nums[l]
        
        """
        ## S1:
        ## Time: O(log(N))
         
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) >> 1
            m_odd = m & 1  # m odd, left side has even number of vals
            # print(l, r, m)
            if nums[m] == nums[m-1]:
                # Case 1: [1, 1, 3, 3, 4, 5, 5]
                if m_odd:  
                    l = m + 1
                # Case 2: [1, 1, 2, 3, 3, 5, 5, 7, 7]
                else:
                    r = m - 2
            elif m + 1 < n and nums[m] == nums[m+1]:
                # Case 3: [1, 1, 2, 3, 3, 5, 5]
                if m_odd:
                    r = m - 1
                # Case 4: [1, 1, 3, 3, 5, 5, 6, 7, 7]
                else:
                    l = m + 2
            else:
                return nums[m]
            
        return nums[m]
        """