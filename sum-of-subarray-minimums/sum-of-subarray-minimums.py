class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        ## S1:
        
        M = 10**9 + 7
        stack = []  # store (val, number) pair
        res = s = 0
        
        for i, x in enumerate(arr):
            cnt = 1
            while stack and stack[-1][0] >= x:
                # need to replace all such stack[-1] with (x, num_x)
                v, n = stack.pop()
                cnt += n
                s -= v * n
            
            stack.append((x, cnt))
            s += x * cnt
            res += s
        
        return res % M  
        