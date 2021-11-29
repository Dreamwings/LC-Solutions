class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        for fr, to in tickets:
            graph[fr].append(to)
            
        for k in graph.keys():
            graph[k].sort(reverse=True)
            # reverse sort to pop out from end
        
        stack = ['JFK']
        res = []
        
        while stack:
            x = stack[-1]
            if x in graph and graph[x]:
                y = graph[x].pop()
                stack.append(y)
            else:
                res.append(x)
                stack.pop()
        
        return res[::-1]        
            
