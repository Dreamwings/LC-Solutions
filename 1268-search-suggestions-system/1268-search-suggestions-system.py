class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        ## S1:
        ## https://leetcode.com/problems/search-suggestions-system/discuss/436674/C%2B%2BJavaPython-Sort-and-Binary-Search-the-Prefix
        ## 
        
        from bisect import bisect_left
        
        p = sorted(products)
        res, prefix, i = [], '', 0
        
        for c in searchWord:
            tmp = []
            prefix += c
            i = bisect_left(p, prefix, i)
            for w in p[i : i + 3]:
                if w.startswith(prefix):
                    tmp.append(w)
            res.append(tmp)
        
        return res