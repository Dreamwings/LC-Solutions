class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        ## S1: DFS
        
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                pre = word[:i]
                suf = word[i:]
                
                if pre in d and suf in d:
                    return True
                elif pre in d and dfs(suf):
                    return True
                # elif dfs(pre) and suf in d:
                #     return True
            
            return False
        
        res = []
        for w in d:
            if dfs(w):
                res.append(w)
                
        return res