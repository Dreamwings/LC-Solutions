class MagicDictionary(object):
    from collections import defaultdict
    
    def __init__(self):
        self.d = defaultdict(set)
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            for i in range(len(word)):
                w = word[:i] + '*' + word[i+1:]
                self.d[w].add(word)
        

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for i in range(len(searchWord)):
            x = searchWord[:i] + '*' + searchWord[i+1:]
            if x in self.d:
                if searchWord not in self.d[x]:
                    return True
                elif len(self.d[x]) > 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)