class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ## S1:
        ## Time O(N)
        ## Space O(1)
        
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res        
        
        