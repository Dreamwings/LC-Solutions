class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
        b = sorted(boxTypes, key=lambda x: (x[1], x[0]), reverse=True)
        res = 0
        
        for i, x in b:
            if i >= truckSize:
                res += x * truckSize
                return res
            else:
                res += x * i
                truckSize -= i
        
        return res