class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        
        s = sum(matchsticks)
        if s % 4: 
            return False
        s, n = s // 4, len(matchsticks)
        
        a = sorted(matchsticks, reverse=True)
        if a[0] > s:
            return False
        res = [0 for _ in range(4)]

        def backtrack(k):
            if k == n:
                return s == res[0] == res[1] == res[2]

            for i in range(4):
                if res[i] + a[k] <= s:
                    res[i] += a[k]
                    ret = backtrack(k + 1)
                    if ret:
                        return True
                    res[i] -= a[k]

                    if res[i] == 0:
                        break

            return False

        return backtrack(0)
        
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