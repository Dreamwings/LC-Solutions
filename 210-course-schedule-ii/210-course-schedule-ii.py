class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        
        ## Solution 1: BFS/Topological Sort
        
        graph = defaultdict(list)
        indeg = {x: 0 for x in range(numCourses)}
        
        for x, y in prerequisites:
            graph[y].append(x)
            indeg[x] += 1
        
        q = deque()
        for k, v in indeg.items():
            if v == 0:
                q.append(k)
        
        if not q: return []
        res = []
        
        while q:
            x = q.popleft()
            res.append(x)
            for y in graph[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
                    
        if len(res) == numCourses:
            return res
        
        return []
        
        """
        
        ## Solution 2: DFS
        res = []
        graph = defaultdict(set)
        out_deg = [0] * numCourses
        q = []
        
        for u, v in prerequisites:
            graph[v].add(u)
            out_deg[u] += 1
        
        for i in range(numCourses):
            if out_deg[i] == 0:
                q.append(i)
        
        if len(q) == 0: return res
        
        while q:
            x = q.pop()
            res.append(x)
            for y in graph[x]:
                out_deg[y] -= 1
                if out_deg[y] == 0:
                    q.append(y)
        
        if len(res) == numCourses: return res
        return []
        """