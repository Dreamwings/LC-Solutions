class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        ## S2: faster than S1
        
        words = set(wordList)
        if beginWord in words: words.remove(beginWord)
        if endWord not in words: return 0
        n = len(beginWord)
        
        q = [beginWord]
        step = 0
        neighbors = collections.defaultdict(set)
        
        for word in words:
            for i in range(n):
                key = word[:i] + "*" + word[i+1:]
                neighbors[key].add(word)
        
        while q:
            nxt = []
            step += 1
            for w in q:
                if w == endWord:
                    return step
                for i in range(n):
                    key = w[:i] + "*" + w[i+1:]
                    for new in neighbors[key]:
                        if new in words:
                            words.remove(new)
                            nxt.append(new)
            
            q = nxt
        
        return 0
                                