class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
        ha = sorted([0] + horizontalCuts + [h])
        wa = sorted([0] + verticalCuts + [w])
        x = max(b - a for a, b in zip(ha, ha[1:]))
        y = max(b - a for a, b in zip(wa, wa[1:]))
        return x * y % int(1e9+7)
        