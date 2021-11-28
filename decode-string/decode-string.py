class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ## S1: Stack
        
        stack = []
        v, res = 0, ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for c in s:
            if c.isdigit():
                v = v * 10 + int(c)
            elif c in letters:
                res += c
            elif c == '[':
                stack.append(res)
                stack.append(v)
                v, res = 0, ''
            elif c == ']':
                pre_v = stack.pop()
                pre_res = stack.pop()
                res = pre_res + res * pre_v
        
        return res
                
        