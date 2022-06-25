class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(cardPoints): 
            return sum(cardPoints)
        
        res = cur = sum(cardPoints[:k])
        
        for i in range(k):
            cur += cardPoints[-1-i]
            cur -= cardPoints[k-1-i]
            res = max(res, cur)
        
        return res