class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) >> 1
            m_odd = m & 1
            # print(l, r, m)
            if nums[m] == nums[m-1]:
                # Case 1: [1, 1, 3, 3, 4, 5, 5]
                if m_odd:  # m odd, left side has even number of vals
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