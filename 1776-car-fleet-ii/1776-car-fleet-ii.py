class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        
        ## S1: Stack
        ## Time: O(N)
        ## Space: O(N)
        
        n = len(cars)
        stack = []  # to store the index of next car
        res = [-1] * n
        
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            while stack:
                j = stack[-1]
                next_p, next_s = cars[j]
                next_hit_t = res[j]
                # two cases:
                # 1. A catchs B and collides
                # 2. A catchs B+C since B catches C and collides first
                if s <= next_s or (next_hit_t > 0 and (next_p - p) * 1.0 / (s - next_s) >= next_hit_t):
                    stack.pop()
                else:
                    break
            
            if stack:
                j = stack[-1]
                next_p, next_s = cars[j]
                res[i] = (next_p - p) * 1.0 / (s - next_s)
                
            stack.append(i)
            
        return res
        