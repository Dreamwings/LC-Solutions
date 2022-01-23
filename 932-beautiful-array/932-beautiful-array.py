class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        """
        ## S1:
        
        res = [1]
        
        while len(res) < n:
            odd, even = [], []
            for x in res:
                odd.append(2 * x - 1)
                even.append(2 * x)
            res = odd + even
        
        return [x for x in res if x <= n]
        """
        
        ## S2:
        ## https://leetcode-cn.com/problems/beautiful-array/solution/piao-liang-shu-zu-by-leetcode/
        ## Time: O(NlogN)
        ## Space: O(NlogN)
        
        
        d = {1: [1]}
        
        def dfs(n):
            if n not in d:
                odd = dfs((n + 1) // 2)
                even = dfs(n // 2)
                d[n] = [2 * x - 1 for x in odd] + [2 * x for x in even]
            return d[n]
        
        return dfs(n)