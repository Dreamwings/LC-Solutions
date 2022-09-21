class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ## S1: DFS Backtracking
        
        words = set(wordDict)
        n = len(s)
        
        def dfs(pos, path):
            if pos == n:
                res.append(path)
                return
            
            for i in range(pos+1, n+1):
                if s[pos:i] in words:
                    if path == '':
                        dfs(i, s[pos:i])
                    else:
                        dfs(i, path + ' ' + s[pos:i])
        
        res = []
        dfs(0, '')
        return res