class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode-cn.com/problems/student-attendance-record-ii/solution/xue-sheng-chu-qin-ji-lu-ii-by-leetcode-s-kdlm/
        
        ## https://leetcode.com/problems/student-attendance-record-ii/discuss/101634/Python-DP-with-explanation
        
        MOD = 10**9 + 7
        
        if n == 1:
            return 3
        
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% MOD)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % MOD
        for i in range(n):
            result += nums[i+1] * nums[n-i] % MOD
            result %= MOD
        return result