class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        ## S1: Stack
        ## Time: O(N)
        ## Space: O(N)
        
        def helper(x):
            stack = []
            for c in x:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        
        a, b = helper(s), helper(t)
        if len(a) != len(b): return False
        
        for x, y in zip(a, b):
            if x != y:
                return False
        
        return True
        