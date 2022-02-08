class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        ## S1: Scan from Right to Left
        ## Time: O(N)
        ## Space: O(1)
        
        for i, x, y in sorted(zip(indices, sources, targets), reverse=True):
            if s[i : i+len(x)] == x:
                s = s[:i] + y + s[i+len(x):]
                
        return s