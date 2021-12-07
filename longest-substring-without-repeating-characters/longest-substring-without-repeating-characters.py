class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        from collections import defaultdict
        
        n = len(s)
        seen = defaultdict(int)  # to store the last index of char
        i = res = 0
        
        for j, c in enumerate(s):
            if c in seen and i <= seen[c]:
                i = seen[c] + 1
            else:
                res = max(res, j - i + 1)
            
            seen[c] = j
        
        return res