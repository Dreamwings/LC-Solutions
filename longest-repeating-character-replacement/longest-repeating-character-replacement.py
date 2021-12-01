class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        from collections import defaultdict
        
        n = len(s)
        d = defaultdict(int)
        i = max_freq = 0
        
        for j, c in enumerate(s):
            d[c] += 1
            max_freq = max(max_freq, d[c])
            
            if j - i + 1 - max_freq > k:
                # need to move left pointer
                d[s[i]] -= 1
                i += 1
        
        return n - i  # j = n - 1 after for loop
        