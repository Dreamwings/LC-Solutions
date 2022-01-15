class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        
        ## S2: faster than S1
        
        d = {c:i for i, c in enumerate(order)}
        
        def comp(a, b):
            i = 0
            while i < len(a) and i < len(b):
                if d[a[i]] < d[b[i]]:
                    return True
                elif d[a[i]] > d[b[i]]:
                    return False
                else:
                    i += 1
            
            if not a[i:]: return True
            else: return False
        
        for a, b in zip(words[:-1], words[1:]):
            if not comp(a, b):
                return False
        
        return True
        
        
        """
        ## S3:
        
        d = {c:i for i, c in enumerate(order)}
        
        a = [[d[c] for c in word] for word in words]
        
        return a == sorted(a)
        
        
        
        
        ## S1:
        
        def comp(a, b):
            i = 0
            while i < len(a) and i < len(b):
                if order.index(a[i]) < order.index(b[i]):
                    return True
                elif order.index(a[i]) > order.index(b[i]):
                    return False
                else:
                    i += 1
            
            if not a[i:]: return True
            else: return False
        
        for a, b in zip(words[:-1], words[1:]):
            if not comp(a, b):
                return False
        
        return True
        """