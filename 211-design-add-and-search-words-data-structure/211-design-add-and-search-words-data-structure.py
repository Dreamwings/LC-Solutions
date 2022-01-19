from collections import defaultdict
class WordDictionary(object):

    def __init__(self):
        self.d = collections.defaultdict(set)

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        n = len(word)
        if n > 0:
            self.d[n].add(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        k = len(word)
        if k not in self.d:
            return False
        if '.' not in word:
            return word in self.d[k]
        
        for w in self.d[k]:
            for x, y in zip(w, word):
                if y != '.' and x != y:
                    break
            else:
                return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)