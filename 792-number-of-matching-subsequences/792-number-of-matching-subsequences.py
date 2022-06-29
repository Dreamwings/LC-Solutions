class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        from collections import defaultdict
        
        d = defaultdict(list)
        res = 0
        
        for w in words:
            d[w[0]].append(w)
        
        for c in s:
            p = d[c]
            del d[c]
            for w in p:
                if len(w) == 1:
                    res += 1
                else:
                    d[w[1]].append(w[1:])
                
        return res