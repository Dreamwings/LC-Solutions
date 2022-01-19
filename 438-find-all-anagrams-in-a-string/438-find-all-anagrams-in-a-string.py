class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        ## Solution 2:
        from collections import defaultdict
        
        n, m = len(s), len(p)
        if n < m: return []
        res = []
        
        d = defaultdict(int)
        
        for c in p:
            d[c] -= 1
        
        for i, c in enumerate(s):
            d[c] += 1
            if d[c] == 0: del d[c]
            if i >= m:
                d[s[i-m]] -= 1
                if d[s[i-m]] == 0:
                    del d[s[i-m]] 
            if len(d) == 0:
                res.append(i-m+1)
        return res
        
        """
        ## Solution 1:
        
        n, m = len(s), len(p)
        if n < m: return []
        res = []
        
        fs, fp = [0] * 26, [0] * 26
        for c in s[:m]:
            fs[ord(c) - ord('a')] += 1
        for c in p:
            fp[ord(c) - ord('a')] += 1
        
        if fs == fp: res.append(0)
        
        for i in range(1, n - m + 1):
            x = ord(s[i-1]) - ord('a')
            y = ord(s[i+m-1]) - ord('a')
            fs[x] -= 1
            fs[y] += 1
            if fs == fp:
                res.append(i)
        
        return res
        """
        