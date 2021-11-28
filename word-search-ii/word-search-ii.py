class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        ## S1: Improved DFS Backtracking
        
        ## add Counter for both board and each word
        ## for a char c, if a word has more c than the board, don't do DFS
        
        from collections import Counter
        
        def dfs(word, pos, x, y, seen):
            # (x, y) is the board cell
            # print(x, y, pos)
            if pos == len(word):
                return True
            
            if (x, y) in seen or x < 0 or x >= m or y < 0 or y >= n:
                return False
            
            if board[x][y] == word[pos]:
                seen.add((x, y))
                dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for dx, dy in dir:
                    i, j = x + dx, y + dy
                    new_pos = pos + 1
                    if dfs(word, new_pos, i, j, seen):
                        return True
                seen.remove((x, y))
            return False
            
        
        m, n = len(board), len(board[0])
        bd = Counter()
        # Note that you can merge two Counters a and b by a + b directly
        for row in board:
            x = Counter(row)
            bd += x
        
        res = []
        
        for w in words:
            # first check if board contains all chars in the word w
            wd = Counter(w)
            has_word = True
            for k, v in wd.items():
                if v > bd[k]:
                    has_word = False
                    break
            if not has_word:
                continue
            
            # if board contains all chars in w, do DFS backtracking
            found = False
            for i in range(m):
                for j in range(n):
                    seen = set()
                    X = dfs(w, 0, i, j, seen)
                    # print(i, j, res, X)
                    if X:
                        res.append(w)
                        found = True
                        break
                if found:
                    break
            
        return res
        