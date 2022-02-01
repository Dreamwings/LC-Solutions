class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ## Solution 2: Sliding Windows (Two Pointers)
        from collections import defaultdict
        
        d = defaultdict(int)  # to store the freq of letters in the window
        n = len(s)
        i = max_freq = 0
        
        for j, c in enumerate(s):
            d[c] += 1
            max_freq = max(max_freq, d[c])
            
            if j - i + 1 - max_freq > k:
                # need to move left pointer
                d[s[i]] -= 1
                i += 1
            
        # return j + 1 - i
        return n - i    # finally j reaches s[n-1] and maitain the max window
            
        """
        ## Solution 1: Sliding Windows (Two Pointers)
        
        cnt = [0] * 26
        n = len(s)
        i = j = 0
        max_freq = 0
        
        while j < n:
            x = ord(s[j]) - ord('A')
            cnt[x] += 1                       # freq of current letter
            max_freq = max(max_freq, cnt[x])  # find the most frequent letter in current window
            if j - i + 1 - max_freq > k:      # more other letters than we can flip, move left pointer; otherwise left pointer stay
                cnt[ord(s[i]) - ord('A')] -= 1
                i += 1
            
            j += 1
        
        return j - i    # (j - i) will always maintain a max window
        """
        
            
        
        