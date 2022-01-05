class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ## S1: DFS Backtracking
        
        def dfs(pos, path):
            if pos == n:
                res.append(' '.join(path))
                
            for i in range(pos + 1, n + 1):
                if s[pos : i] in words:
                    dfs(i, path + [s[pos : i]])
        
        n = len(s)
        words = set(wordDict)
        res = []
        dfs(0, [])
        return res