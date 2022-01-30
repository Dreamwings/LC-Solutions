class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        
        ## S2:
        
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