class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = {c: i for i, c in enumerate(order)}
        
        def comp(x, y):
            i = 0
            while i < len(x) and i < len(y):
                if d[x[i]] < d[y[i]]:
                    return True
                elif d[x[i]] > d[y[i]]:
                    return False
                else:
                    i += 1
            if not x[i:]: return True
            return False
        
        for a, b in zip(words[:-1], words[1:]):
            if not comp(a, b):
                return False
            
        return True    
                
        
        