class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -x:
                    stack.pop()
                if stack and stack[-1] + x == 0:
                    stack.pop()
                    continue
                if not stack or stack[-1] < 0:
                    stack.append(x)
                    
        return stack
        