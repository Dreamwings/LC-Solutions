class Solution:
    def totalStrength(self, nums: List[int]) -> int:
        ## S2:
        ## https://leetcode.cn/problems/sum-of-total-strength-of-wizards/solution/dan-diao-zhan-qian-zhui-he-de-qian-zhui-d9nki/
        ## Time: O(N)
        ## Space: O(N)
        
        from itertools import accumulate
        
        n = len(nums)
        M = 10 ** 9 + 7
        if n == 1:
            return nums[0] * nums[0] % M
        
        lmin = [-1] * n # lmin[i] is the nearest index for min val on the left of i, if doesn't exist, -1
        rmin = [n] * n # rmin[i] is the nearest index for min val on the right of i, if doesn't exist, n
        stack = []
        res = 0
        
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] > x:
                j = stack.pop()
                rmin[j] = i
            if stack:
                lmin[i] = stack[-1]
            stack.append(i)
        
        # presum of presum
        acc = list(accumulate(accumulate(nums), initial = 0))
        for i in range(n):
            l, r = lmin[i], rmin[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += nums[i] * (racc * ln - lacc * rn)
        return res % M
        
        
        
        