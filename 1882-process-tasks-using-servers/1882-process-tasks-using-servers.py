class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        
        ## S1: Heapq
        ## Time: O(T*lg(S)) S the length of servers, T the length of tasks
        ## Space: O(S+T)
        
        res = []
        h1 = [[weight, i ,0] for i, weight in enumerate(servers)]
        h2 = []
        heapq.heapify(h1)
        for j, task in enumerate(tasks):
            while h2 and h2[0][0] <= j or not h1:
                time, weight, i = heapq.heappop(h2)
                heapq.heappush(h1, [weight, i, time])
            weight, i, time = heapq.heappop(h1)
            res.append(i)
            heapq.heappush(h2, [max(time,j)+task, weight, i])
        return res
        