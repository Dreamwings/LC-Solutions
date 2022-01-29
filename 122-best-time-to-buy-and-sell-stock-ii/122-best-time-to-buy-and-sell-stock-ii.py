class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        ## S1: Greedy
        
        n = len(prices)
        if n == 1: return 0
        
        profit = 0
        
        for a, b in zip(prices[:-1], prices[1:]):
            if a < b:
                profit += b - a
            
        return profit
        