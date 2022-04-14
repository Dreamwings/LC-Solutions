class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        seen = collections.defaultdict(int)  # to store the last index of char
        i = 0
        res = 0
        
        for j, c in enumerate(s):
            if c in seen and i <= seen[c]:
                i = seen[c] + 1
            else:
                res = max(res, j - i + 1)
            seen[c] = j
            
        return res    
        