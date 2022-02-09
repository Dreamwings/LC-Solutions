class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
        from collections import defaultdict
        
        ## S1: BFS
        
        d = defaultdict(set)
        for i, r in enumerate(routes):
            for x in r:
                d[x].add(i)
        
        q = [(source, 0)]
        seen = set([source])
        
        for x, cnt in q:
            if x == target:
                return cnt
            for i in d[x]:
                for y in routes[i]:
                    if y not in seen:
                        q.append((y, cnt + 1))
                        seen.add(y)
                routes[i] = []
            
        return -1            
        
        # while q:
        #     next_q = []
        #     for x, cnt in q:
        #         if x == target:
        #             return cnt
        #         for i in d[x]:
        #             for y in routes[i]:
        #                 if y not in seen:
        #                     next_q.append((y, cnt + 1))
        #                     seen.add(y)
        #             routes[i] = []
        #     q = next_q
        # return -1            
        