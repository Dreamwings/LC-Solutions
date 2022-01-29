class Solution:
    def calculate(self, s: str) -> int:
        
        res, v, sign = 0, 0, 1
        stack = []
        
        for c in s:
            if c.isdigit():
                v = 10 * v + int(c)
            elif c == '+' or c == '-':
                res += v * sign
                v = 0
                # sign = 1 if c == '+' else -1
                sign = [-1, 1][c == '+']
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign * v
                res *= stack.pop() # pop out the prev sign before '('
                res += stack.pop() # pop out the prev res before '('
                v = 0
        
        res += v * sign
        return res
        
        