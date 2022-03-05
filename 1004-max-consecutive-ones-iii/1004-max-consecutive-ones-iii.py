class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        ## Solution 1: Two Pointers with a Moving Window
        """
        i = 0
        
        for j, x in enumerate(A):
            K -= (1 - x)
            if K < 0: # Need to move the left pointer
                K += (1 - A[i])
                i += 1
            # print(i, j)
        return j - i + 1
        """
        
        l = 0
        for r, x in enumerate(A):
            K -= (1 - x)
            if K < 0:
                K += (1 - A[l])
                l += 1
                
        return r - l + 1