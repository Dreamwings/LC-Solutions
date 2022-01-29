class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res, v, sign = 0, 0, 1
        stack = [] # used when there is '()'
        
        for c in s:
            if c.isdigit():
                v = 10 * v + int(c)
            elif c in '+-':
                res += sign * v
                v = 0
                sign = [-1, 1][c == '+'] # note first one is False, second one is True
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign * v
                res *= stack.pop() # the sign before '('
                res += stack.pop() # prev res before '('
                v = 0
        
        res += sign * v
        return res