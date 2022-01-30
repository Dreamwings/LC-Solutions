class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        
        cnts = [0] * 121
        for age in ages:
            cnts[age] += 1
            
        res = 0
        for i in range(1,121):
            if cnts[i]:
                k = int(i* 0.5 + 7)
                res += cnts[i] * sum(cnts[k+1:i])
                if i > k:
                    res += cnts[i] * (cnts[i] - 1)
        return res