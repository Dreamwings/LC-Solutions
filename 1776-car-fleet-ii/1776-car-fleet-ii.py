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
            # print(i, stack)
            p, s = cars[i]
            while stack:
                j = stack[-1]
                next_p, next_s = cars[j]
                next_hit_t = res[j]
                # two cases:
                # 1. A catchs B and collides, s > next_s
                # 2. A catchs B+C since B catches C and collides first, next_hit_t is the time B catches C
                #    tmp = (next_p - p) * 1.0 / (s - next_s)
                #    tmp >= next_hit_t > 0, with this case, neet to pop last i from stack, but check the previous stack val
                if s <= next_s:
                    # Case 1: no collision
                    stack.pop()
                elif next_hit_t > 0 and (next_p - p) * 1.0 / (s - next_s) >= next_hit_t:
                    # Case 2: no collision
                    stack.pop()
                else: # has collision
                    break
            
            if stack:
                j = stack[-1]
                next_p, next_s = cars[j]
                res[i] = (next_p - p) * 1.0 / (s - next_s)
                
            stack.append(i)
            
        return res
        