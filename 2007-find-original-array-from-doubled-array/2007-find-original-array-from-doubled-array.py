class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        
        d = Counter(changed)
        res = []
        
        for x in sorted(changed):
            if x == 0:  # 0 * 2 = 0, special case
                if d[x] & 1:  # odd number of 0, invalid
                    return []
            if d[x] == 0:  # when x is a double of another, must be considered before the next case
                continue
            if d[2 * x] == 0: # when x is small, it must have 2 * x
                return []
            res.append(x)
            d[x] -= 1
            d[2 * x] -= 1
        
        return res
        