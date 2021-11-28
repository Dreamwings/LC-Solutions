class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        
        ## S2: DFS
        
        from collections import defaultdict
        
        g = defaultdict(list)
        
        for u, v in adjacentPairs:
            g[u].append(v)
            g[v].append(u)
            
        q = []
        for k, v in g.items():
            if len(v) == 1:
                q.append(k)
                break
        
        seen = set()
        res = []
        while q:
            x = q.pop()
            res.append(x)
            seen.add(x)
            for y in g[x]:
                if y not in seen:
                    q.append(y)
        
        return res
        
        
        """
        ## S1: DFS
        
        from collections import defaultdict
        
        g = defaultdict(list)
        
        for u, v in adjacentPairs:
            g[u].append(v)
            g[v].append(u)
            
        head = None
        for k, v in g.items():
            if len(v) == 1:
                head = k
                break
        
        seen = set()
        res = []
        def dfs(x):
            res.append(x)
            seen.add(x)
            for y in g[x]:
                if y not in seen:
                    dfs(y)
            
        dfs(head)
        return res
        """
        