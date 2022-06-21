class Solution:
    def calculate(self, s: str) -> int:
        
        res, v, sign = 0, 0, 1
        stack = []
        
        for c in s:
            if c.isdigit():
                v = 10 * v + int(c)
            elif c in "+-":
                res += v * sign
                sign = [-1, 1][c == '+']
                v = 0
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ")":
                res += sign * v
                res *= stack.pop()
                res += stack.pop()
                v = 0
                sign = 1
                
        res += sign * v
        return res
                
        
        