class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        ## Solution 4: DFS
        
        r, c, n = len(s1), len(s2), len(s3)
        if r + c != n: return False
        
        q, seen = [(0, 0)], set()
        
        while q:
            i, j = q.pop()
            if i + j == n:
                return True
            seen.add((i, j))
            
            if i < r and s1[i] == s3[i+j] and ((i+1, j)) not in seen:
                q.append((i+1, j))
            
            if j < c and s2[j] == s3[i+j] and ((i, j+1)) not in seen:
                q.append((i, j+1))
            
        return False
        