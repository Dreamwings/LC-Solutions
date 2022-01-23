class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ## https://leetcode.com/problems/beautiful-array/discuss/1368125/Detailed-Explanation-with-Diagrams.-A-Collection-of-Ideas-from-Multiple-Posts.-Python3
        
        """
        ## S1: Iterative
        
        res = [1]
        
        while len(res) < n:
            odd = [2 * x - 1 for x in res]
            even = [2 * x for x in res]
            res = odd + even
            
        # print(res)
        return [x for x in res if x <= n]
        """
        
        ## S2: DFS
        
        d = {1: [1]}
        
        def dfs(n):
            if n not in d:
                odd = dfs((n + 1) // 2)
                even = dfs(n // 2)
                d[n] = [2 * x - 1 for x in odd] + [2 * x for x in even]
            return d[n]
        
        return dfs(n)
        
        