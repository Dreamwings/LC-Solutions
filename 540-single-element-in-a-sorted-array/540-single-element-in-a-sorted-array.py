class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
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
            