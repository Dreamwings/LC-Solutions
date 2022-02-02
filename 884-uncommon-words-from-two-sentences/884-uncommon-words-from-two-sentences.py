class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
        from collections import Counter
        
        set1 = Counter(s1.split(' '))
        set2 = Counter(s2.split(' '))
        res = []
        
        for w, f in set1.items():
            if w in set2:
                del set2[w]
            elif f == 1:
                res.append(w)
        for w, f in set2.items():
            if f == 1:
                res.append(w)
        
        return res