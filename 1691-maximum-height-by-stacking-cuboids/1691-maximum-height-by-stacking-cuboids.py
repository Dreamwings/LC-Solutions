class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        
        ## S1: DP with Sort
        ## https://leetcode.com/problems/maximum-height-by-stacking-cuboids/discuss/970293/JavaC%2B%2BPython-DP-Prove-with-Explanation
        ## https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids/solution/python3-ba-mei-ge-chang-fang-ti-xuan-zhu-ljem/
        ## Time: O(N^2)
        ## Space: O(N)
        
        n = len(cuboids)
        for a in cuboids:
            a.sort(reverse=True)  # set a[0] as height, which is the largest of W, L, H
        
        cuboids.sort(reverse=True) # put ones with largest H in the front, which should be at the bottom
        dp = [0] * n
        
        for i in range(n):
            dp[i] = cuboids[i][0]
            for j in range(i):
                if cuboids[j][1] >= cuboids[i][1] and cuboids[j][2] >= cuboids[i][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][0])
                    
        return max(dp)