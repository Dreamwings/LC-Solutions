class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        stack = [['_', 0]]
        res = ''
        
        for c in s:
            if c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        for c, x in stack:
            res += c * x
            
        return res    
