class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        
        ## S2: DFS Backtracking
        
        s = sum(matchsticks)
        if s % 4:
            return False
        s, n = s // 4, len(matchsticks)
        
        a = sorted(matchsticks, reverse=True)
        if a[0] > s:
            return False
        
        edge = [0, 0, 0, 0]
        
        def dfs(pos):
            if pos == n:
                return s == edge[0] == edge[1] == edge[2] == edge[3]
            
            for i in range(4):
                if edge[i] + a[pos] > s:
                    continue
                edge[i] += a[pos]
                if dfs(pos + 1):
                    return True
                
                # if not work out, do backtracking
                edge[i] -= a[pos]
                if edge[i] == 0:
                    break
            
            return False
        
        return dfs(0)
                
        
        """
        ## S1: Time Limit Exceeded
        
        s = sum(matchsticks)
        if s % 4: 
            return False
        s, n = s // 4, len(matchsticks)
        
        a = sorted(matchsticks, reverse=True)
        if a[0] > s:
            return False
        
        def dfs(i, s1, s2, s3, s4):
            if i == n:
                return s1 == s2 == s3 == s4 == s
                
            if s1 > s or s2 > s or s3 > s or s4 > s:
                return False
            
            res = False
            for k in range(4):
                if k == 0:
                    res = res or dfs(i+1, s1 + a[i], s2, s3, s4)
                if k == 1:
                    res = res or dfs(i+1, s1, s2 + a[i], s3, s4)
                if k == 2:
                    res = res or dfs(i+1, s1, s2, s3 + a[i], s4)
                if k == 3:
                    res = res or dfs(i+1, s1, s2, s3, s4 + a[i])
            
            return res
        
        return dfs(0, 0, 0, 0, 0)
        """ 