class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        ## Solution 3: Beat 99%
        

        wset = set(wordList)
        if beginWord in wset: wset.remove(beginWord)
        if endWord not in wset: return []
        
        n = len(beginWord)
        paths = defaultdict(set)
        found, rev = False, False
        bq, eq, nq = {beginWord}, {endWord}, set()
        
        while bq and not found:
            wset -= set(bq)
            for word in bq:
                for i in range(n):
                    pre_word, suf_word = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = pre_word + c + suf_word
                        if new_word in wset:
                            if new_word in eq:
                                found = True
                            else:
                                nq.add(new_word)
                            if rev:
                                paths[new_word].add(word)
                            else:
                                paths[word].add(new_word)
                                
            bq, nq = nq, set()
            if len(bq) > len(eq): # change direction
                bq, eq, rev = eq, bq, not rev
            
        # def bt(x): # backtracking (DFS) for solution
        #     if x == endWord:
        #         return [[x]]
        #     else:
        #         return [[x] + rest for y in paths[x] for rest in bt(y)]
        # return bt(beginWord)
    
        res = []
        
        def bfs(word, cur_path):
            if word == endWord:
                cur_path.append(word)
                res.append(cur_path)
                return
            else:
                for parent in paths[word]:
                    bfs(parent, cur_path+[word])
        bfs(beginWord, [])
        return res
        
                
        
        """
        
        ## S2: 
        
        words = set(wordList)
        if beginWord in words: words.remove(beginWord)
        if endWord not in words: return []
        
        n = len(beginWord)
        neighbors = defaultdict(list)
        for w in words:
            for i in range(n):
                key = w[:i] + '*' + w[i+1:]
                neighbors[key].append(w)
        
        q = [(beginWord, [beginWord])]
        res = []
        seen = set()
        
        while q:
            nxt = []
            curr_seen = set()
            for w, path in q:
                if w == endWord:
                    res.append(path)
                for i in range(n):
                    key = w[:i] + '*' + w[i+1:]
                    for new in neighbors[key]:
                        if new not in seen: # not seen in previous levels
                            nxt.append((new, path + [new]))
                            curr_seen.add(new)
                                
            if res and res[0][-1] == endWord: return res
            q = nxt
            seen |= curr_seen
        
        return []
        
        
        
        ## S1:
        
        wset = set(wordList)
        if beginWord in wset: wset.remove(beginWord)
        if endWord not in wset: return []
        n = len(beginWord)
        paths = defaultdict(list)
        paths[beginWord] = [[beginWord]]
        
        while paths:
            new_paths = defaultdict(list)
            for word in paths:
                if word == endWord:
                    return paths[word]
                
                for i in range(n):
                    first, second = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        # print(i, c)
                        new = first + c + second
                        if new in wset:
                            new_paths[new] += [path + [new] for path in paths[word]]
                            # print(new_paths)
            wset -= set(paths.keys())
            paths = new_paths
        
        return []
        
        
        """
        
            
            
            
            
            