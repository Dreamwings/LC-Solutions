class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in range(32):
            zeros = ones = 0
            for x in nums:
                lsb = (x >> i) & 1
                ones += lsb
                zeros += (1 - lsb)
            
            res += ones * zeros
            
        return res