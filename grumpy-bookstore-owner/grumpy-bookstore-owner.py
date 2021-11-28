class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        ## S1: Sliding Window
        
        i, res = 0, 0
        satisfied, to_satisfy = 0, 0
        
        for c, g in zip(customers, grumpy):
            if g == 0:
                satisfied += c
            else:
                to_satisfy += c
            
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    to_satisfy -= customers[i - minutes]
            
            res = max(res, to_satisfy)
            i += 1
        
        return satisfied + res