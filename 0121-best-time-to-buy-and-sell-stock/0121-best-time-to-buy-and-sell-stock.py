class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        m, res = prices[0], 0
        
        for x in prices[1:]:
            m = min(m, x)
            res = max(res, x - m)
        
        return res