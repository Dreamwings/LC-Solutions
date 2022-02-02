class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        from bisect import bisect, insort
        
        ## S1: insort
        ## Time: O(N logK) 
        ## https://leetcode.com/problems/sliding-window-median/discuss/96337/Python-SortedArray-(beats-100)-and-2-Heap(beats-90)-solution
        
        win, rv = nums[:k], []
        win.sort()
        odd = k%2
        for i,n in enumerate(nums[k:],k):
            rv.append((win[k/2]+win[k/2-1])/2. if not odd else win[(k-1)/2]*1.)
            win.pop(bisect(win, nums[i-k])-1) # <<< bisect is faster than .remove()
            insort(win, nums[i])
        rv.append((win[k/2]+win[k/2-1])/2. if not odd else win[(k-1)/2]*1.)
        return rv
    
    
        