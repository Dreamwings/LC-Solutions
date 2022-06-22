class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import defaultdict, deque
        
        ## Solution 1: BFS/Topological Sort
        
        g = defaultdict(list)
        indeg = {i: 0 for i in range(numCourses)}
        
        for x, y in prerequisites:
            g[y].append(x)
            indeg[x] += 1
        
        q = deque()
        
        for k, v in indeg.items():
            if v == 0:
                q.append(k)
        
        res = []
        if not q: return res
        
        while q:
            x = q.popleft()
            res.append(x)
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
       
        if len(res) == numCourses:
            return res
        return []
            