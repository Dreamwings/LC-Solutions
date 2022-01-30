class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from collections import defaultdict
        
        
        ## S 2: BFS
        ## Special level traversal BFS
        
        cur_stop = defaultdict(int)
        cur_stop[0] = 1
        
        for dist in nums:
            next_stop = defaultdict(int)
            for stop, cnt in cur_stop.items():
                next_stop[stop + dist] += cnt
                next_stop[stop - dist] += cnt
            cur_stop = next_stop
                
        return cur_stop[target]
    
        
        """
        
        ## S 1: DFS + Memorization (TLE)
        ## https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.
        
        
        def dfs(i, target, path_sum):
            if i == n and path_sum == target:
                return 1
            elif i == n:
                return 0
            
            pos = dfs(i+1, target, path_sum + nums[i])
            neg = dfs(i+1, target, path_sum - nums[i])
            
            return pos + neg
        
        n = len(nums)
        res = dfs(0, target, 0)
        
        return res
        
        
        """