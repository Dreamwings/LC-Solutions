class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        a = candidates
        n = len(a)
        
        def dfs(pos, path, t):
            if t < 0: return
            if t == 0:
                res.append(path)
                return
            
            for i in range(pos, n):
                dfs(i, path + [a[i]], t - a[i])
        
        res = []
        dfs(0, [], target)
        return res