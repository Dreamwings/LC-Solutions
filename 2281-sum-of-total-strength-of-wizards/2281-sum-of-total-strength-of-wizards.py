class Solution(object):
    def totalStrength(self, nums):
        """
        :type strength: List[int]
        :rtype: int
        """
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
        n = len(strength)
        M = 10 ** 9 + 7
        if n == 1: return strength[0] * strength[0] % M

        res = 0
        s, stack, acc = 0, [-1], [0]
        strength.append(0)

        for r, x in enumerate(strength):
            s += x
            acc.append(s + acc[-1])
            while stack and strength[stack[-1]] > x:
                i = stack.pop()
                l = stack[-1]
                lacc = acc[i] - acc[max(l, 0)]
                racc = acc[r] - acc[i]
                ln, rn = i - l, r - i
                res += strength[i] * (racc * ln - lacc * rn) % M
            stack.append(r)
        
        return res % M
        """