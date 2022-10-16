class Solution(object):
    def totalStrength(self, nums):
        """
        :type strength: List[int]
        :rtype: int
        """
        ## S1: 
        ## https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2061985/JavaC%2B%2BPython-One-Pass-Solution
        ## Time: O(N)
        ## Space: O(N)
        
        n = len(nums)
        M = 10 ** 9 + 7
        if n == 1:
            return nums[0] * nums[0] % M
        
        s = 0 # prefix sum
        stack = [-1] # to store the index of min val for subarray ended at current val
        acc = [0] # to store sum of presum
        nums += [0]
        res = 0
        # l [............ i ............] r
        # l: last min index
        # i: current min index
        # r: next min index
        
        for r, x in enumerate(nums):
            s += x
            acc.append(s + acc[-1])
            while stack and nums[stack[-1]] > x:
                i = stack.pop()
                l = stack[-1]
                lacc = acc[i] - acc[max(0, l)]  # sum of presum between l and i
                racc = acc[r] - acc[i]          # sum of presum between i and r
                # for ']' at any place between i and r, it always count nums[i] * lacc
                # for '[' at any place between l and i, it always count nums[i] * racc
                res += nums[i] * (racc * (i - l) - lacc * (r - i))
                res %= M
                
            stack.append(r)
            
        return res % M
        
        """
                
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
        
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] >= x:
                j = stack.pop()
                rmin[j] = i
                if stack:
                    lmin[i] = stack[-1]
                stack.append(i)
        
        # presum of presum
        ss = list(accumulate(accumulate(nums, initial=0), initial=0))
        res = 0
        
        for i, x in enumerate(nums):
            l, r = lmin[i], rmin[i]  # (l, r) both sides are open
            s = (i - l) * (ss[r+1] - ss[i+1]) - (r - i) * (ss[i+1] - ss[l+1])
            res += x * s
            res %= M
            
        return res % M
        
        
        
        """
