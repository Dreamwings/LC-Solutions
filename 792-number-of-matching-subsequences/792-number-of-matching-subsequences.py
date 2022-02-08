class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        
        ## S1:
        ## to understand: https://leetcode-cn.com/problems/number-of-matching-subsequences/solution/pi-pei-zi-xu-lie-de-dan-ci-shu-by-leetcode/
        ## https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation
        
        d = collections.defaultdict(list)
        res = 0
        
        for w in words:
            d[w[0]].append(w)
        
        for x in s:
            possible_words = d[x]
            d[x] = []  # remove this item, but will add new ones
            
            for w in possible_words:
                if len(w) == 1:  # there is a match for single letter string
                    res += 1
                else:
                    d[w[1]].append(w[1:])
        
        return res