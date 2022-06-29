class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        ##
        ## e.g.
        ## s = "abcde"
        ## words = ["a","bb","acd","ace", "bde", "ce"]
        
        from collections import defaultdict
        
        d = defaultdict(list)
        res = 0
        
        for w in words:
            d[w[0]].append(w)
        # print(d)
        for c in s:
            p = d[c]
            del d[c]
            for w in p:
                if len(w) == 1:
                    res += 1
                else:
                    d[w[1]].append(w[1:])
            # print(d)
        return res