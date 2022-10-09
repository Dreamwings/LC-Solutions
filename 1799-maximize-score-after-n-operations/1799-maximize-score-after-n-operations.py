class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode.cn/problems/maximize-score-after-n-operations/solution/cpython3-zhuang-ya-dp-by-hanxin_hanxin-azsb/
        
        def gcd(a, b):
            while b != 0:
                tmp = a % b
                a = b
                b = tmp
            return a

        #最多14个数字，摆明了是让状态压缩
        n = len(nums)

        #---- 预计算一下gcd数组，虽然只有14个数字，但是数字都很大
        g = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                g[i][j] = g[j][i] = gcd(nums[i], nums[j])

        dp = [0 for _ in range(1 << n)]
        for state in range(1, 1 << n):
            cnt1 = (bin(state)[2:]).count('1')
            if cnt1 % 2 == 0:   #偶数个，2个2个的用，必剩偶数
                operation = cnt1 // 2
                for i in range(n):
                    for j in range(i + 1, n):
                        if (state >> i) & 1 and (state >> j) & 1:
                            dp[state] = max(dp[state], dp[state - (1 << i) - (1 << j)] + operation * g[i][j])

        return dp[(1<<n) - 1]

        
