class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        lets, digs = [], []
        
        for log in logs:
            if log[-1].isdigit():
                digs.append(log)
            else:
                lets.append((log.split(' ', 1)))
        
        lets.sort(key=lambda x: (x[1], x[0]))
        
        res = []
        for a, b in lets:
            res.append(a + ' ' + b)
        
        res += digs
        return res
        