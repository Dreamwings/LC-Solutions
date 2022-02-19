class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        
        a = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        n = len(a)
        hq, res = [], []
        i = 0
        t = a[0][0]
        
        while len(res) < n:
            while i < n and a[i][0] <= t:
                heappush(hq, (a[i][1], a[i][2]))  # (proc time, task index)
                i += 1
                # print(hq, res)
            if hq:
                pt, idx = heappop(hq)
                res.append(idx)
                t += pt
            elif i < n:
                t = a[i][0]
            
        return res