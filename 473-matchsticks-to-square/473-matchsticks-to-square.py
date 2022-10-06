class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
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
                
                
                
        