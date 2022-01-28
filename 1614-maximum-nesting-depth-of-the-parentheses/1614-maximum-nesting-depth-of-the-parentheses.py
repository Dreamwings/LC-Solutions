class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res, cnt = 0, 0
        
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            res = max(res, cnt)
            
        return res