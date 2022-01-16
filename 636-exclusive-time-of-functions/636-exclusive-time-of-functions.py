class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0] * n
        stack = [] # store function id
        prev = 0
        
        for log in logs:
            i, se, t = log.split(':')
            i, t = int(i), int(t)
            
            if se == 'start':
                if stack:
                    pre_i = stack[-1]
                    res[pre_i] += t - prev
                prev = t
                stack.append(i)
            else:
                pre_i = stack.pop()
                res[pre_i] += t + 1 - prev
                prev = t + 1
        
        return res
    
        """
        
        ## S2:
        
        res = [0] * n
        stack = []
        time = []
        
        for log in logs:
            i, se, t = log.split(':')
            i, t = int(i), int(t)
            
            if se == 'start':
                stack.append(i)
                time.append(t)
            else:
                x = stack.pop()
                tlen = t - time.pop() + 1
                res[x] += tlen
                if stack:
                    res[stack[-1]] -= tlen
        
        return res
    
        """