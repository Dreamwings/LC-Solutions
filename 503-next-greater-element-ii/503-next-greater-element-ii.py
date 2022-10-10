class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        if n == 1: return [-1]
        res = [-1] * n
        stack = []
        
        for i in range(2 * n - 1):
            i %= n
            while stack and nums[stack[-1]] < nums[i]:
                j = stack.pop()
                res[j] = nums[i]
            stack.append(i)
        
        return res    