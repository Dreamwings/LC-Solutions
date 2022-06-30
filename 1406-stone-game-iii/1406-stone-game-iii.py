class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        
        ## S2: DP
        ## https://leetcode-cn.com/problems/stone-game-iii/solution/shi-zi-you-xi-iii-by-leetcode-solution/
        
        # first calculate suffix sum of stoneValue
        n = len(stoneValue)
        suf_sum = [0] * (n-1) + [stoneValue[-1]]
        
        for i in range(n-2, -1, -1):
            suf_sum[i] = suf_sum[i+1] + stoneValue[i]
        
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = suf_sum[i] - min(dp[i+1 : i+4])
            # print(dp)
            
        if dp[0] * 2 == suf_sum[0]:
            return "Tie"
        elif dp[0] * 2 > suf_sum[0]:
            return "Alice"
        else:
            return "Bob"
        
        """
        ## S1: DP
        ## https://leetcode.com/problems/stone-game-iii/discuss/564260/JavaC%2B%2BPython-DP-O(1)-Space
        ## Time: O(N)
        ## Space: O(1)
        
        dp = [0] * 3
        n = len(stoneValue)
        
        for i in range(n-1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i : i+k]) - dp[(i + k) % 3] for k in [1, 2, 3])
        
        if dp[0] == 0:
            return 'Tie'
        elif dp[0] > 0:
            return 'Alice'
        else:
            return 'Bob'
        
        """
        