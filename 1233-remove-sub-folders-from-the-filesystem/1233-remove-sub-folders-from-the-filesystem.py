class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort()
        res = [folder[0]]
        
        for s in folder[1:]:
            x = res[-1]
            if x not in s:
                res.append(s)
            elif s.index(x) != 0:
                res.append(s)
            else:
                n = len(x)
                if s[n] != '/':
                    res.append(s)
        
        return res
        