class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## S1:
        ## https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/
        ## Time: O(N)
        
        # for any array whose length is N, the first missing positive must be in range [1,...,N+1]
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # print(nums)
        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])
        # print(nums)
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
        
        """
        ## S2: 
        ## Time: O(N)
        ## for any array whose length is l, the first missing positive must be in range [1,...,l+1]
        
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1,len(nums)):
            if nums[i] / n==0:
                return i
        return n
        
        
        ## S3:
        
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res
        
        """