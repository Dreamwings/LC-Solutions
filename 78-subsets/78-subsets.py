class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ## Solution 1: DFS
        ## Time: O(N * 2^N)
        
        def dfs(pos, path):
            res.append(path)
            
            for i in range(pos, n):
                dfs(i + 1, path + [nums[i]])
        
        n = len(nums)
        res = []
        dfs(0, [])
        
        return res
        
        """
        ## Solution 2:
        ## Time: O(N * 2^N)
        
        res = [[]]
        
        for x in nums:
            cur = res[:]
            for a in cur:
                res.append(a + [x])
        
        return res
        
        """
        