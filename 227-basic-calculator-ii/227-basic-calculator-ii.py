class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        v = 0
        pre_op = '+'
        s += '+'
        
        for c in s:
            if c in '0123456789':
                v = 10 * v + int(c)
            elif c in '+-*/':
                if pre_op == '+':
                    stack.append(v)
                elif pre_op == '-':
                    stack.append(-v)
                elif pre_op == '*':
                    x = stack.pop()
                    stack.append(x * v)
                elif pre_op == '/':
                    x = stack.pop()
                    stack.append(int(x/v))
                v, pre_op = 0, c
                
        return sum(stack)