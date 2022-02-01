class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s += '+'
        v, pre_op, stack = 0, '+', []
        
        for c in s:
            if c.isdigit():
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
                    # The following is only for Python 2
                    # Python 3 can handle it well with: int(x/y)
                    stack.append(int(x * 1.0 / v))
                v, pre_op = 0, c
                    
        return sum(stack)            
            
            