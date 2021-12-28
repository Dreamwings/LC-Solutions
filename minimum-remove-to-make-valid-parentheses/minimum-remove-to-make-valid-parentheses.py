class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        ## S1: Stack
        
        stack = []
        cur = '' # the substring inside current ()
        
        for c in s:
            if c == '(': # start a new string or new parentheses
                stack.append(cur)
                cur = ''
            elif c == ')':
                # it means it should be like: '(cur)'
                if stack: 
                    # stack must not be empty because it should have '(' previously
                    # otherwise it's not a valid one
                    cur = stack.pop() + '(' + cur + ')'
            else:
                cur += c
            # print(c, cur, stack)
            
        res = ''.join(stack)
           
        res += cur
        return res
        """
        
        ## S2: 
        
        cnt = 0
        res = ''
        
        for c in s:
            if c == '(':
                res += c
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    continue
                else:
                    cnt -= 1
                    res += c
            else:
                res += c
        
        if cnt > 0:
            tmp = res[::-1]
            res = ''
            i = 0
            while cnt > 0:
                if tmp[i] == '(':
                    cnt -= 1
                else:
                    res += tmp[i]
                i += 1
            res += tmp[i:]
            res = res[::-1]
        
        return res
                    
                
                    
        
        