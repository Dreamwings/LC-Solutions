class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## S2: Greedy
        ## Time: O(N)
        ## Space: O(1)
        
        # let two var to record scores: if '(', both += 1; if ')', both -= 1; if '*', left -= 1 and right += 1
        l = r = 0
        
        for c in s:
            if c == '(':
                l += 1
                r += 1
            elif c == ')':
                l -= 1
                r -= 1
            else:
                l -= 1
                r += 1
            l = max(0, l)
            if r < 0:  # too many ')'
                return False
        
        return l == 0
        
        """
        ## S1: Stack
        ## Time: O(N)
        ## Space: O(N)
        
        left_s, star_s = [], []  # two stacks to store index of '(' and '*'
        
        for i, c in enumerate(s):
            if c == '(':
                left_s.append(i)
            elif c == '*':
                star_s.append(i)
            else:
                if left_s:
                    left_s.pop()
                elif star_s:
                    star_s.pop()
                else:
                    return False
        
        while left_s:
            if not star_s:
                return False
            elif star_s[-1] < left_s[-1]: # last '*' on the left of last '('
                return False
            else:
                left_s.pop()
                star_s.pop()
                
        return True    
        """