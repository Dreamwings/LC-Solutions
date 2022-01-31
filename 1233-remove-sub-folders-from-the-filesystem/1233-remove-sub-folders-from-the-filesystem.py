class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
        folder.sort()
        res = [folder[0]]
        i = 1
        
        while i < len(folder):
            if res[-1] not in folder[i]:
                res.append(folder[i])
            elif folder[i].index(res[-1]) != 0:
                res.append(folder[i])
            else:
                x = len(res[-1])
                if folder[i][x] != '/':
                    res.append(folder[i])
            i += 1
        
        return res
        