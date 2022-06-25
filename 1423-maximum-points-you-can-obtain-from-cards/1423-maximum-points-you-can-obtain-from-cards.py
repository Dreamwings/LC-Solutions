class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        ## S1:
        ## Refer the figure here: 
        ## https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597825/Simple-Clean-Intuitive-Explanation-with-Visualization
        ## Time: O(N)
        ## Space: O(1)
        
        
        if k >= len(cardPoints): 
            return sum(cardPoints)
        
        res = cur = sum(cardPoints[:k])
        
        for i in range(k):
            cur += cardPoints[-1-i]
            cur -= cardPoints[k-1-i]
            res = max(res, cur)
        
        return res