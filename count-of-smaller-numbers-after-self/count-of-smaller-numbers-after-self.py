class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ## S1: Bisect
        ## Time: O(NlogN)
        ## https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/bu-dao-10xing-dai-ma-zui-jian-dan-fang-fa-mei-you-/
        
        from bisect import bisect_left, insort
        
        res = []
        a = []
        # a is the sorted array
        
        for x in nums[::-1]:
            i = bisect_left(a, x)
            res.append(i)
            insort(a, x)
        
        return res[::-1]