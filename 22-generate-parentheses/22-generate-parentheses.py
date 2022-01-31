class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ## S 1: DFS, also BackTracking
        ## https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
        
        def dfs(l, r, path, res):
            if l > r: return
            if not l and not r:
                res.append(path)
                return
            if l:
                dfs(l-1, r, path + '(', res)
            if r:
                dfs(l, r-1, path + ')', res)
        
        res = []
        dfs(n, n, '', res)
        return res
    
        """
        
        ## S 2: Iterative DFS
        
        stack = [('(', 1, 0)]
        res = []
        
        while stack:
            path, l, r = stack.pop()
            if l < r or l > n or r > n:
                continue
            if l == r == n:
                res.append(path)
            
            stack.append((path + '(', l + 1, r))
            stack.append((path + ')', l, r + 1))
        
        return res
        
        
        """
        
        