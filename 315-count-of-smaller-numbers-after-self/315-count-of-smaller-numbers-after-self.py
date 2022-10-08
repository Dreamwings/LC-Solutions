class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        from bisect import bisect_left, insort
        
        a, res = [], []
        # a is to store the sorted elements from the right of nums
        
        for x in nums[::-1]:
            i = bisect_left(a, x) # this is the number of smaller elements to the right of x
            res.append(i)
            insort(a, x)
        
        return res[::-1]