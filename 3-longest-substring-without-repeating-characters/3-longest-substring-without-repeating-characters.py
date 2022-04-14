class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        
        if not s: return 0
        seen = defaultdict(int)   # to store the last index of char
        i, res = 0, 0
        
        for j, c in enumerate(s):
            if c in seen and i <= seen[c]:
                i = seen[c] + 1
            else:
                res = max(res, j - i + 1)
            seen[c] = j
            
        return res