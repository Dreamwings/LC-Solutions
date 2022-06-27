class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        
        res = pre = 0
        
        for x in target:
            res += max(0, x - pre)
            pre = x
            
        return res
        