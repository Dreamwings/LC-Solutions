class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ## S2: Memorization:
        ## Time: O(N), N is the number of operators in the input
        
        # use a dict to store sub expressions res
        from collections import defaultdict
        
        mem = defaultdict(list)
        
        def dfs(l, r):
            if s[l:r].isdigit():
                return [int(s[l:r])]
            
            if (l, r) in mem:
                return mem[(l, r)]
        
            res = []
            
            for i, c in enumerate(s[l:r]):
                if c in '+-*':
                    l_res = dfs(l, l + i)      # be careful!
                    r_res = dfs(l + i + 1, r)  # be careful!
                    for x in l_res:
                        for y in r_res:
                            if c == '+':
                                res.append(x + y)
                            elif c == '-':
                                res.append(x - y)
                            elif c == '*':
                                res.append(x * y)
            mem[(l, r)] = res
            return res
        
        return dfs(0, len(s))
        
        
        """
        ## S1: DFS (Divide and Conquer)
        ## Time: O(N^2), N is the number of operators in the input
        
        if s.isdigit():
            return [int(s)]
        
        res = []
        
        for i, c in enumerate(s):
            if c in '+-*':
                l_res = self.diffWaysToCompute(s[:i])
                r_res = self.diffWaysToCompute(s[i+1:])
                for x in l_res:
                    for y in r_res:
                        if c == '+':
                            res.append(x + y)
                        if c == '-':
                            res.append(x - y)
                        if c == '*':
                            res.append(x * y)
        
        return res
        """                