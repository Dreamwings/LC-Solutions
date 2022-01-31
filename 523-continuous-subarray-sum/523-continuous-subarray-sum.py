class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        ## S1: 
        
        # note that k >= 1
        # use dict d to store the remainder of presum mod k and its first index
        # key is remainder, value is index
        d = {0: -1}
        s = 0
        
        for i, x in enumerate(nums):
            s += x
            s %= k
            
            if s not in d:
                d[s] = i
            else:
                if i - d[s] >= 2:
                    return True
        
        return False